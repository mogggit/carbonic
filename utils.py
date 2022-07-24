from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_email(subject, embody):
    # flaskemail of google account
    sender = 'flask.pyone@gmail.com'
    password = 'yrqioxjnlkykjife'
    # email
    content = MIMEMultipart()
    content['subject'] = subject
    content['from'] = sender
    content['to'] = 'pyone.tw@gmail.com'
    # content.attach(MIMEText('主機時間'))
    content.attach(MIMEText(embody, 'html'))

    with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:
        try:
            # 驗證 SMTP 伺服器
            smtp.ehlo()
            # 建立加密傳輸
            smtp.starttls()
            smtp.login(sender, password)
            smtp.send_message(content)
        except Exception as e:
            pass

def get_now():
    import pytz
    from datetime import datetime
    taipei = pytz.timezone('Asia/Taipei')
    now = datetime.now(taipei)
    return now

def get_datetime():
    now = get_now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def get_nowid():
    now = get_now()
    return now.strftime("%y%m%d%H%M")

def get_sha2(stext):
    import hashlib

    opt = input('1.SHA-256  2.SHA-384  3.SHA-512: ')[0]
    if opt not in '123':
        return
    elif opt == '1':
        sha2 = '256'
    elif opt == '2':
        sha2 = '384'
    elif opt == '3':
        sha2 = '512'
    hashcode = eval(f"hashlib.sha{sha2}(stext.encode('utf8')).hexdigest()")
    print(hashcode)
    print()


if __name__ == '__main__':
    print('datetime:', get_datetime())
    print('nowid:', get_nowid())
    while True:
        print('a. Get SHA-2 Hash')
        print('b. Test Gmail')
        print('q. Quit')
        op = input('> ').lower()
        if op == 'q':
            break
        elif op == 'a':
            while True:
                stext = input('Input a text to get SHA-2 hash (q. Quit): ')
                if stext.lower() in ('q', 'quit'):
                    break
                else:
                    get_sha2(stext)
        elif op == 'b':
            while True:
                embody = input('Input email body (q. Quit): ')
                if embody.lower() in ('q', 'quit'):
                    break
                else:
                    subject = f'Email Test ({get_now()})'
                    send_email(subject, embody)
        print()