// hide menu after click menu item
$(document).on('click','.navbar-collapse',function(e) {
    if( $(e.target).is('a') && ( $(e.target).attr('class') != 'dropdown-toggle' ) ) {
        $(this).collapse('hide');
    }
});

// scrolltop
$(window).scroll(function() {
    if ($(this).scrollTop() > 50 ) {
        $('.scrolltop:hidden').stop(true, true).fadeIn();
    } else {
        $('.scrolltop').stop(true, true).fadeOut();
    }
});
$(function(){$(".scroll").click(function(){$("html,body").animate({scrollTop:$(".thetop").offset().top},"1000");return false})})

// copy code to clipboard
// <script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/1.7.1/clipboard.min.js"></script>
var pre = document.getElementsByTagName('pre');
for (var i = 0; i < pre.length; i++) {
    var button = document.createElement('button');
    button.className = 'btn btn-copy btn-secondary';
    button.textContent = 'Copy';
    pre[i].insertBefore(button, pre[i].firstChild);
}
var copyCode = new Clipboard('.btn-copy', {
   	text: function (trigger) {
        var origText = $(trigger).next().text().replace(/\n\            /g, '\n');
        origText = origText.replace('\n', '');
        // origText = origText.replace('\n        ', '\n');
        return origText;
    }
});