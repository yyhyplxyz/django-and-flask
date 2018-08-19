from flask import jsonify, request, flash, render_template
from flask_login import current_user

from app.models.gift import Gift
from app.models.wish import Wish
from app.templates.trade import Trade_info
from app.viewmodels.book import Book_viewmodel,Book_collection
from app.forms.book import searchform
from app.web import web
from app.spider.fishbook import fishbook
from app.libs.helper import is_isbn_or_key
import json


@web.route('/book/search') #不要把视图函数都放在一个文件里，或者不要都放在入口文件里
def search():
    # q = request.args['q'] #根据本地代理实现
    # page = request.args['page']
    #验证层
    form = searchform(request.args)
    books = Book_collection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushubook = fishbook()
        if isbn_or_key == 'isbn':
            yushubook.searchbyisbn(q)
            # res = fishbook.searchbyisbn(q)
            # res = Book_viewmodel.package_single(res, q)
        else:
            yushubook.searchbykeyword(q,page)
        #__dict__会返回变量的字典形式，能解决序列化问题
        books.fill(yushubook, q)
        # return json.dumps(books, default=lambda o: o.__dict__)
            # res = fishbook.searchbykeyword(q,page)
            # res = Book_viewmodel.package_collection(res, q)
        # return jsonify(books)
    else:
        flash('搜索的关键字不符合要求，请重新搜索')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books)

    #单页面业务逻辑主要在前端完成
    #多页面业务逻辑主要在服务器运算完成
@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gift = False
    has_in_wish = False

    yushubook = fishbook()
    yushubook.searchbyisbn(isbn)
    book = Book_viewmodel(yushubook.first)
    if current_user.is_authenticated:
        if Gift.query.filter_by(uid = current_user.id, isbn=isbn, launched=False).first():
            has_in_gift = True
        if Wish.query.filter_by(isbn = isbn, launched=False).first():
            has_in_wish = True


    trade_gift = Gift.query.filter_by(isbn = isbn, launched=False).all()
    trade_wish = Wish.query.filter_by(isbn=isbn,launched=False).all()
    trade_wish_detail = Trade_info(trade_wish)
    trade_gift_detail = Trade_info(trade_gift)


    return render_template('book_detail.html',book=book,wishes=trade_wish_detail,gifts=trade_gift_detail,
                           has_in_gift = has_in_gift,
                            has_in_wish = has_in_wish)

#MVC 业务逻辑是写在model层中的