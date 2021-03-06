from flask import Flask

from app.models.base import db
from flask_login import LoginManager
from flask_mail import Mail

loginmanager = LoginManager()
mail = Mail()
def create_app():
    app = Flask(__name__) #决定了根目录是app，而不是fisher，可以指定static_folder,static_url

    # 蓝图 blueprint来实现分文件功能 app->蓝图->视图函数 wen是一个蓝图

    # 载入配置文件, 配置文件规定只能写大写， DEBUG是模块中的默认值 为false， 如果有小写的，就会出错
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    db.init_app(app)
    #以下是两种方法，第三种方法是在初始化db时传入app
    # with app.app_context():
    #     db.create_all()
    loginmanager.init_app(app)
    loginmanager.login_view = 'web.login' #致命登陆的视图函数，需要登陆时自动跳转
    loginmanager.login_message = '请先登录或注册'
    mail.init_app(app)
    with app.app_context():
        db.create_all(app = app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)