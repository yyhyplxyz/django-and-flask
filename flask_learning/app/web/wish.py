from flask import flash, render_template, redirect, url_for

from app.libs.email import send_email
from app.models.base import db
from app.models.gift import Gift
from app.models.wish import Wish
from app.viewmodels.wish import Mywishes
from . import web
from flask_login import login_required, current_user

__author__ = '七月'


@web.route('/my/wish')
def my_wish():
    uid = current_user.id
    wishes_of_mine = Wish.get_user_wishes(uid)
    isbn_list = [wish.isbn for wish in wishes_of_mine]
    gift_count_list = Wish.get_gifts_counts(isbn_list)
    view_model = Mywishes(wishes_of_mine, gift_count_list)
    return render_template('my_wish.html', wishes=view_model.gifts)


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
@login_required
def satisfy_wish(wid):
    """
            向想要这本书的人发送一封邮件
            注意，这个接口需要做一定的频率限制
            这接口比较适合写成一个ajax接口
        """
    wish = Wish.query.get_or_404(wid)
    gift = Gift.query.filter_by(uid=current_user.id, isbn=wish.isbn).first()
    if not gift:
        flash('你还没有上传此书，请点击“加入到赠送清单”添加此书。添加前，请确保自己可以赠送此书')
    else:
        send_email(wish.user.email, '有人想送你一本书', 'email/satisify_wish.html', wish=wish,
                   gift=gift)
        flash('已向他/她发送了一封邮件，如果他/她愿意接受你的赠送，你将收到一个鱼漂')
    return redirect(url_for('web.book_detail', isbn=wish.isbn))


@web.route('/wish/book/<isbn>/redraw')
@login_required
def redraw_from_wish(isbn):
    wish = Wish.query.filter_by(isbn=isbn).first()
    if not wish:
        flash('该心愿不存在，删除失败')
    else:
        with db.auto_commit():
            wish.status = 0
    return redirect(url_for('web.my_wish'))
