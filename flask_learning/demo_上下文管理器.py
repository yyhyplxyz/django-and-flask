class Myresource:
    # def __enter__(self):
    #     print("connect resource")
    #     return self #返回上下文管理器
    # def __exit__(self, exc_type, exc_val, exc_tb): #要有四个参数
    #     if exc_tb:
    #         print('process exception')
    #     else:
    #         print('no exception')
    #
    #     print("close resource")
    #     return False #外部仍可以抛出异常，如果返回True，内部抛出了异常后，外部不会再抛出异常了

    def query(self):
        print("query")

with Myresource() as resource:
    resource.query()


from contextlib import contextmanager
@contextmanager #将非上下文管理器变成上下文管理器
def make_myresource():
    print('connect to resource', end='\n') #指明结束符号是什么
    yield Myresource()
    print('close resource connection')

#yield 生成器 返回之后继续执行后面的语句
with make_myresource() as r:
    r.query()