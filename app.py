import os
import sys
import random
import time
import urllib.request
import json
from datetime import date, timedelta
from functools import wraps
from werkzeug.local import LocalProxy
from flask import Flask, render_template, send_from_directory
from flask import session, request, redirect, url_for, current_app
import utils

app = Flask(__name__)
log = LocalProxy(lambda: current_app.logger)
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
# SHA-256 from 'flaskblank'
app.config['SECRET_KEY'] = 'ad4daf864b7ef595f5bbb6d1d55aca53c4e1c959827327e91ab15478b5164d9a'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)
cyear = date.today().year
nowid = lambda: utils.get_nowid()
dtnow = lambda: utils.get_datetime()

@app.before_request
def before_request():
    if 'DYNO' in os.environ:
        if request.url.startswith('http://'):
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if session.get('is_auth') is None:
            return redirect(url_for('index'))
        return func(*args, **kwargs)
    return decorated_function


@app.route('/', methods=['GET', 'POST'])
def index():
    submit_result = ''
    if request.method == 'POST':
        # log.info(request.form)
        # 密碼與帳號相同
        dict_roles = {
              'admin': '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918',
            'student': '264c8c381bf16c982a4e59b0dd4c6f7808c51a05f64c35db42cc78a2a72875bb',
            'teacher': '1057a9604e04b274da5a4de0c8f4b4868d9b230989f8c8c6a28221143cc5a755',
        }
        if 'selRole' in request.form and 'txtPassword' in request.form:
            the_role = request.form.get('selRole')
            if the_role in dict_roles and request.form.get('txtPassword') == dict_roles[the_role]:
                session['is_auth'] = True
                session['role_name'] = the_role
                session['account'] = the_role
                return redirect(url_for('home'))
            elif the_role not in dict_roles:
                submit_result = '登入失敗：身份識別錯誤'
            else:
                submit_result = '登入失敗：通行密碼錯誤'
        else:
            return redirect(url_for('denied'))
    return render_template('login-home.html', submit_result=submit_result, cyear=cyear, nowid=nowid())

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    next_url = 'home'
    session.clear()
    return redirect(url_for(next_url))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico', mimetype='image/x-icon')

@app.route('/robots.txt')
def robots():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'robots.txt', mimetype='text/plain')

@app.route('/denied')
def denied():
    return render_template("denied.html", cyear=cyear, nowid=nowid())

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", cyear=cyear, nowid=nowid()), 404

@app.route('/home')
@login_required
def home():
    # log.info(session)
    return render_template('home.html', cyear=cyear, dtnow=dtnow(), nowid=nowid())

@app.route('/flaskweb/movies/<act_id>')
@login_required
def movies(act_id):
    json_file = open(os.path.join(app.root_path, 'templates/flaskweb/movies.json'), encoding='utf-8').read()
    list_movies = json.loads(json_file)
    return render_template('flaskweb/movies.html', nowid=nowid(), act_id=act_id, list_movies=list_movies)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)