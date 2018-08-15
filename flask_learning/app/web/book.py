from flask import jsonify, request
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
            yushubook.searchbykeyword(q.page)
        #__dict__会返回变量的字典形式，能解决序列化问题
        books.fill(yushubook, q)
        return json.dumps(books, default=lambda o: o.__dict__)
            # res = fishbook.searchbykeyword(q,page)
            # res = Book_viewmodel.package_collection(res, q)
        # return jsonify(books)
    else:
        return jsonify(form.errors)

    #单页面业务逻辑主要在前端完成
    #多页面业务逻辑主要在服务器运算完成
