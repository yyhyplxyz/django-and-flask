from flask import current_app

from app.models.base import *

from sqlalchemy import *
from sqlalchemy.orm import relationship
from app.spider.fishbook import fishbook
from collections import namedtuple

class Gift(Base):
    id = Column(Integer, primary_key = True)
    launched = Column(Boolean, Default = False)
    user = relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)

    @classmethod #类代表礼物，实例代表一个礼物，这个最近礼物函数是对类而言的
    def recent(cls):
        recent_gift = Gift.query.filter_by(launched=False).group_by(
        Gift.isbn).order_by(desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']
        ).distinct().all()
        #链式调用，非常灵活

        return recent_gift

    #能抽象出具体业务的尽量写在model层里，写在视图函数较fuza
    #新建service层没有意义
    @property
    def book(self):
        yushubook = fishbook()
        yushubook.searchbyisbn(self.isbn)
        return yushubook.first

    @classmethod
    def get_user_gifts(cls,uid):
        gifts = Gift.query.filter_by(launched=False).order_by(desc(Gift.create_time)).all()

        return gifts

    @classmethod
    def get_wish_counts(cls,isbn_list):
        #接受条件表达式
        #没有重写filter函数
        #分组统计功能
        #更适合跨表查询
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(Wish.launched == False,
                                      Wish.isbn.in_(isbn_list),
                                      Wish.status == 1).group_by(
            Wish.isbn
        ).all()
        #countlist是个元组列表，每个元组有两个内容
        #不应返回元组列表 而应返回字典
        count_list = [{'count':w[0], 'isbn':w[1]} for w in count_list]
        return count_list


from app.models.wish import Wish
