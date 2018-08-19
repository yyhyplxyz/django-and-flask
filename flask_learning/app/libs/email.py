from threading import Thread
from flask import current_app, render_template

from app import mail
from flask_mail import Message

def send_async_email(app, msg): #启动新新线程时，因为线程隔离，request和app栈都是空的
    #不要传递代理对象即可
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            raise e


def send_email(to, subject, template, **kwargs):
    # msg = Message('Test mail', sender='yang_yuanhao@foxmail.com',
    #               body='Testing', recipients=['user@qq.com'])
    msg = Message('[Yang Yuanhao]' + ' ' + subject, sender=current_app.config['MAIL_SENDER']
                  ,recipients=[to])
    msg.html = render_template(template, **kwargs)
    thr = Thread(target=send_async_email, args=[current_app._get_current_object(),msg])
    thr.start()
#current app是个代理对象，每次读取current app都是读app栈顶元素
#app=Flask（）则是一个实例化的对象


