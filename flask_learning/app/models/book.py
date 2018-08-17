#sqlalchemy -> flask-sqlachemy 高度封装
#wtforms ->flaskWtfroms
from sqlalchemy import Column, Integer, String, Boolean, Float
from app.models.base import Base
from flask_sqlalchemy import SQLAlchemy



class book(Base):
    id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(String(50), nullable=False)
    author = Column(String(50), default='未名')
    isbn = Column(String(15), nullable=False, unique = True)
    price = Column(String(20))
    binding = Column(String(20))
    publisher = Column(String(50))
    pages = Column(Integer)
    pubdate = Column(String(20))
    summary = Column(String(1000))
    image = Column(String(50))
    def sample(self):
        pass