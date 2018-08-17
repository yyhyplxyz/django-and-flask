from sqlalchemy import Column, Integer, String, SmallInteger
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True #不会创建一个真正的表
    create_time= Column('create_time', Integer)
    status = Column(SmallInteger, default=1) #逻辑删除，判断是否删除，不是物理删除

    def set_attrs(self, attrs_dict):
        for k, v in attrs_dict.items():
            if hasattr(self,k) and k != 'id':
                setattr(self,k,v)
        