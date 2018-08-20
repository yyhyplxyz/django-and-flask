from app.libs.enums import PendingStatus
from sqlalchemy import Column, String, Integer, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship
from app.models.base import Base


class Drift(Base):
    """
        一次具体的交易信息
    """
    __tablename__ = 'drift'

    def __init__(self):
        self.pending = PendingStatus.waiting
        super(Drift, self).__init__()

    id = Column(Integer, primary_key=True)
    recipient_name = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)
    message = Column(String(200))
    mobile = Column(String(20), nullable=False)
    isbn = Column(String(13))
    book_title = Column(String(50))
    book_author = Column(String(30))
    book_img = Column(String(50))
    # requester_id = Column(Integer, ForeignKey('user.id'))
    # requester = relationship('User')
    requester_id = Column(Integer)
    requester_nickname = Column(String(20))
    gifter_id = Column(Integer)
    gift_id = Column(Integer)
    gifter_nickname = Column(String(20))
    _pending = Column('pending', SmallInteger, default=1)
    # gift_id = Column(Integer, ForeignKey('gift.id'))
    # gift = relationship('Gift')
    #没有进行模型关联，而是有数据冗余
    #模型关联可以让多个数据段同步更改
    #冗余信息可以保存历史状态，比如淘宝订单的价格，对有记录性质的字段不要做模型关联
    #数据冗余会导致数据不一致，但较少了数据查询次数

    @property #将数字转化成枚举类型， getter方法
    def pending(self):
        return PendingStatus(self._pending)

    @pending.setter #将枚举转化成数字类型
    def pending(self, status):
        self._pending = status.value
