from flask import flash, redirect, url_for, render_template, request, current_app

from app.forms.book import DriftForm
from app.libs.email import send_email
from app.libs.enums import PendingStatus
from app.models.base import db
from app.models.drift import Drift
from app.models.gift import Gift, desc
from app.models.user import User
from app.models.wish import Wish
from app.viewmodels.drift import DriftCollection
from . import web
from sqlalchemy import or_
from flask_login import logout_user, login_required, current_user


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    currend_gift = Gift.query.get_or_404(gid)
    if currend_gift.is_yourself_gift(current_user.id):
        flash('不能向自己索要书籍')
        return redirect(url_for('web.book_detail', isbn=currend_gift.isbn))
    can = current_user.can_send_drift()
    if not can:
        return render_template('not_enough_beans.html', beans=current_user.beans)
    form = DriftForm(request.form)
    if request.method == 'POST' and form.validate():
        save_drift(form,currend_gift)
        send_email(currend_gift.user.email, '有人想要一本书', 'email/get_gift'
                   , wisher=current_user,
                   gift=currend_gift)
    gifter = currend_gift.user.summary
    return render_template('drift.html', gifter = gifter, user_beans
                           = current_user.beans)


@web.route('/pending')
@login_required
def pending():
    # drifts = Drift.query.filter_by(
    #     request.id == current_user.id,
    # gifter_id = current_user.id).order_by(
    #     desc(Drift.create_time)
    # ).all() #and的查询

    #or的查询
    drifts = Drift.query.filter(or_(
        request.id == current_user.id,
        gifter_id=current_user.id).order_by(
        desc(Drift.create_time)
    )
    ).all()
    views = DriftCollection(drifts, current_user.id)
    return render_template('pending.html', drifts=views.data)



@web.route('/drift/<int:did>/reject')
@login_required
def reject_drift(did):
    with db.auto_commit():
        drift = Drift.query.filter_by(Gift.uid == current_user.id,
                                      Drift.id == did).first_or_404()
        drift.pending = PendingStatus.reject
        requester = User.query.get_or_404(drift.requester_id)
        requester.beans += 1
    return redirect(url_for('web.pending'))


@web.route('/drift/<int:did>/redraw')
@login_required #不能防止超权，用户可能修改url的编号进行非法操作
def redraw_drift(did):
    with db.auto_commit():
        drift = Drift.query.filter_by(id == did, requester_id == current_user.id).first_or_404()
        drift.pending = PendingStatus.redraw
        current_user.beans += 1
    return redirect(url_for('web.pending'))


@web.route('/drift/<int:did>/mailed')
@login_required
def mailed_drift(did):
    with db.auto_commit():
        # requester_id = current_user.id 这个条件可以防止超权
        drift = Drift.query.filter_by(
            gifter_id=current_user.id, id=did).first_or_404()
        drift.pending = PendingStatus.success
        current_user.beans += current_app.config['BEANS_EVERY_DRIFT']
        gift = Gift.query.filter_by(id=drift.gift_id).first_or_404()
        gift.launched = True
        # 不查询直接更新;这一步可以异步来操作
        Wish.query.filter_by(isbn=drift.isbn, uid=drift.requester_id,
                             launched=False).update({Wish.launched: True})
    return redirect(url_for('web.pending'))

def save_drift(drift_form,current_gift):
    with db.auto_commit():
        drift = Drift()
        drift_form.populate_obj(drift)
        #form和model的名称相同才能复制
        drift.gift_id = current_gift.id
        drift.requester_id = current_user.id
        drift.requester_nickname = current_user.nickname
        drift.gifter_id = current_gift.user.id
        drift.gifter_nickname = current_gift.user.nickname
        # drift.message = DriftForm.message.data

        book = current_gift.book.first
        drift.book_title = book['title']
        drift.book_author = book['author']
        drift.book_img = book['img']
        drift.isbn = book['isbn']

        current_user.beans -= 1

        db.session.add(drift)




