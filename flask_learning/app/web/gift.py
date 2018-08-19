from flask import current_app

from app.models.base import db
from app.models.gift import Gift
from . import web
from flask_login import login_required, current_user
__author__ = '七月'

@login_required #权限分级是通过改写loginrequired实现的
@web.route('/my/gifts')
def my_gifts():

    pass

@login_required
@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    gift = Gift()
    gift.isbn = isbn
    gift.uid = current_user.id #根据getuser方法，login模块自动实现模型的转换关联
    current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
    db.session.add(gift)
    db.session.commit()

@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



