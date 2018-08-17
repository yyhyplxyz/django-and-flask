from app.models.base import *

from sqlalchemy import *
from sqlalchemy.orm import relationship

class Gift(Base):
    id = Column(Integer, primary_key = True)
    launched = Column(Boolean, Default = False)
    user = relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    
