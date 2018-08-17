from app.models.base import Base
from sqlalchemy import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
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

        
    def check_password(self, raw):
        check_password_hash(self._password, raw)