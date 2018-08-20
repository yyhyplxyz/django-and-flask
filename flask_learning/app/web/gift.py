from flask import current_app, flash, render_template, redirect, url_for

from app.libs.enums import PendingStatus
from app.models.base import db
from app.models.drift import Drift
from app.models.gift import Gift
from app.viewmodels.gift import Mygifts
from . import web
from flask_login import login_required, current_user

@login_required #权限分级是通过改写loginrequired实现的
@web.route('/my/gifts')
def my_gifts():
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    wish_count_list = Gift.get_wish_counts(isbn_list)
    view_model = Mygifts(gifts_of_mine, wish_count_list)
    return render_template('my_gifts.html', gifts=view_model.gifts)

@login_required
@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    if current_user.cansavetolist(isbn):
        #rollback
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id  # 根据getuser方法，login模块自动实现模型的转换关联
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        #可以使用ajax技术实现返回之前页面，避免重复刷新
        #也可以使用页面缓存技术
        flash('这本书已添加至愿望清单或想要清单，请不要重复添加')
    return

@web.route('/gifts/<gid>/redraw')
@login_required
def redraw_from_gifts(gid):
    gift = Gift.query.filter_by(id=gid, launched=False).first()
    if not gift:
        flash('该书籍不存在，或已经交易，删除失败')
    drift = Drift.query.filter_by(gift_id=gid, pending=PendingStatus.waiting).first()
    if drift:
        flash('这个礼物正处于交易状态，请先前往鱼漂完成该交易')
    else:
        with db.auto_commit():
            current_user.beans -= current_app.config['BEANS_UPLOAD_ONE_BOOK']
            gift.delete()
    return redirect(url_for('web.my_gifts'))



