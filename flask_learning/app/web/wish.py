from flask import flash

from app.models.base import db
from app.models.wish import Wish
from . import web
from flask_login import login_required, current_user

__author__ = '七月'


@web.route('/my/wish')
def my_wish():
    pass

@login_required
@web.route('/wish/book/<isbn>')
def save_to_wish(isbn):
    if current_user.cansavetolist(isbn):
        #rollback
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id  # 根据getuser方法，login模块自动实现模型的转换关联
            db.session.add(wish)
    else:
        #可以使用ajax技术实现返回之前页面，避免重复刷新
        #也可以使用页面缓存技术
        flash('这本书已添加至愿望清单或想要清单，请不要重复添加')


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
