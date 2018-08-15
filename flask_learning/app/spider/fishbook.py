from app.libs.Myhttp import HTTP
from flask import current_app #一个代理

from fisher import app


class fishbook:
    # per_page = 15
    #模型层 MVC中的M层

    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    def __init__(self):
        self.total = 0
        self.books = []

    def searchbyisbn(self, isbn):
        url = self.isbn_url.format(isbn)
        reslut = HTTP.get(url)
        #以下是缓存的伪代码，减少访问api的频率次数
        # book = query_from_mysql(isbn)
        # if book:
        #     return book
        # else:
        #     save(res)
        self.__fill_single(reslut)
        # return reslut


    def searchbykeyword(self, keyword, page=1):
        url = self.isbn_url.format(keyword,current_app.config['PRE_PAGE'],self.calculate(page))
        reslut = HTTP.get(url)
        self.__fill_collection(reslut)
        # return reslut

    def calculate(self, page):
        return current_app.config['PRE_PAGE'] * (page - 1)

    def __fill_single(self,data):
        if data:
            self.total = 1
            self.books.append(data)
    def __fill_collection(self,data):
        self.books = data['books']
        self.total = data['total']


#先检查app_stack 当其为空时，推入app进app栈，当来请求时，推入request stack
#请求结束时，两个栈元素都会被推出
#请求中不需要手动推入app，否则需要手动推入app (离线应用和单元测试时）
# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.confif['DEBUG']
# ctx.pop()

#实现了__enter__ 和 __exit__ 就是上下文管理器
#上面三行代码等价于
# with app.app_context():
#     a = current_app
#     d = current_app.confif['DEBUG']
