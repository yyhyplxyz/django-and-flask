from sqlalchemy import Column, Integer, String, SmallInteger
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from contextlib import contextmanager
from datetime import datetime

class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        super(Query.self).filter_by(**kwargs) #传入字典时需要对字典进行解包


db = SQLAlchemy(query_class=Query)
class Base(db.Model):
    __abstract__ = True #不会创建一个真正的表
    create_time= Column('create_time', Integer) #不能在这里写default，类变量是所有对象共享的变量，不是实例变量，会在启动服务器时初始化
    status = Column(SmallInteger, default=1) #逻辑删除，判断是否删除，不是物理删除
    def __init__(self):
        self.create_time = int(datetime.now().timestamp())
    def set_attrs(self, attrs_dict):
        for k, v in attrs_dict.items():
            if hasattr(self,k) and k != 'id':
                setattr(self,k,v)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def delete(self):
        self.status = 0
