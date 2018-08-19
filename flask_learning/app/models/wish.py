from app.models.base import *

from sqlalchemy import *
from sqlalchemy.orm import relationship


from app.spider.fishbook import fishbook


class Wish(Base):
    id = Column(Integer, primary_key=True)
    launched = Column(Boolean, Default=False)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)

    @classmethod
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(launched=False).order_by(desc(Wish.create_time)).all()

        return wishes

    @classmethod
    def get_gifts_counts(cls, isbn_list):
        # 接受条件表达式
        # 没有重写filter函数
        # 分组统计功能
        # 更适合跨表查询
        count_list = db.session.query(func.count(Gift.id), Wish.isbn).filter(Gift.launched == False,
                                                                             Gift.isbn.in_(isbn_list),
                                                                             Gift.status == 1).group_by(
            Gift.isbn
        ).all()
        # countlist是个元组列表，每个元组有两个内容
        # 不应返回元组列表 而应返回字典
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushubook = fishbook()
        yushubook.searchbyisbn(self.isbn)
        return yushubook.first

from app.models.gift import Gift #这里产生了循环导入