from flask import Blueprint

web = Blueprint('web', __name__) #蓝图是为了拆分模块的, 也可以指定staticfolder和static url

from app.web import book
from app.web import user
from app.web import auth
from app.web import gift
from app.web import  wish
from app.web import drift
from app.web import main