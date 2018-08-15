from app.libs.Myhttp import HTTP
from flask import current_app #一个代理

from fisher import app


class fishbook:
    # per_page = 15
    #模型层 MVC中的M层

    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    def __init__(self):
        pass

    @classmethod
    def searchbyisbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        reslut = HTTP.get(url)
        return reslut
    @classmethod
    def searchbykeyword(cls, keyword, page=1):
        url = cls.isbn_url.format(keyword,current_app.config['PRE_PAGE'],cls.calculate(page))
        reslut = HTTP.get(url)
        return reslut

    @classmethod
    def calculate(cls, page):
        return current_app.config['PRE_PAGE'] * (page - 1)

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

class Myresource:
    def __enter__(self):
        print("connect resource")
        return self #返回上下文管理器
    def __exit__(self, exc_type, exc_val, exc_tb): #要有四个参数
        print("close resource")

    def query(self):
        print("query")

with Myresource() as resource:
    resource.query()