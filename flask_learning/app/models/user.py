from app.libs.helper import is_isbn_or_key
from app.models.base import Base
from sqlalchemy import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import  loginmanager
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.fishbook import fishbook


class User(Base, UserMixin):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column('password', String(128), nullable=False)
    _password = Column(String(128))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw):
        self._password = generate_password_hash(raw)
    #override usermixin getid method
    def get_id(self):
        return self.id

    def cansavetolist(self,isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushbook = fishbook()
        yushbook.searchbyisbn(isbn)
        if not yushbook.first:
            return False
        #既不在心愿清单也不在愿望清单才能保存到列表
        gifting = Gift.query.filter_by(uid = self.id,
                                       isbn = isbn,launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id,
                                       isbn=isbn, launched=False).first()
        if not gifting and not wishing:
            return True
        else:
            return False
        
    def check_password(self, raw):
        check_password_hash(self._password, raw)

@loginmanager.user_loader #在app里导入了loginmanager
def get_user(uid):
    return User.query.get(int(uid))