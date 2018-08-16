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
        url = self.keyword_url.format(keyword,current_app.config['PRE_PAGE'],self.calculate(page))
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
    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None


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

#jiajia是一个模板语言，我们可以自己更改模板语言类型，对字典和对象的访问方式是一样的 if和for in要在百分号里，且必须类似latex闭合
#竖线作为值的过滤
# 根据end point反向寻找文件，保证了修改static文件夹位置时，不会改变过多代码
# url_for('static', filename) redertemplate不是通过路由，不可以使用此方法


#set_flash_messge 消息闪现,多个消息组成列表, 一个block里定义的消息 set  只在这个作用域内起作用 with和endwith可以进一步限制作用域
# flash("hello, qiyue", category='errors')