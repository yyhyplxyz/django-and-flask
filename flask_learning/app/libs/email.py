from flask import current_app, render_template

from app import mail
from flask_mail import Message
def send_email(to, subject, template, **kwargs):
    # msg = Message('Test mail', sender='yang_yuanhao@foxmail.com',
    #               body='Testing', recipients=['user@qq.com'])
    msg = Message('[Yang Yuanhao]' + ' ' + subject, sender=current_app.config['MAIL_SENDER']
                  ,recipients=[to])
    msg.html = render_template(template, **kwargs)
    mail.send(msg)
