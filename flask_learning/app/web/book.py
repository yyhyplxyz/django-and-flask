from flask import jsonify, request
from app.viewmodels.book import Book_viewmodel
from app.forms.book import searchform
from app.web import web
from app.spider.fishbook import fishbook
from app.libs.helper import is_isbn_or_key


@web.route('/book/search') #不要把视图函数都放在一个文件里，或者不要都放在入口文件里
def search():
    # q = request.args['q'] #根据本地代理实现
    # page = request.args['page']
    #验证层
    form = searchform(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            res = fishbook.searchbyisbn(q)
            res = Book_viewmodel.package_single(res, q)
        else:
            res = fishbook.searchbykeyword(q,page)
            res = Book_viewmodel.package_collection(res, q)
        return jsonify(res)
    else:
        return jsonify(form.errors)