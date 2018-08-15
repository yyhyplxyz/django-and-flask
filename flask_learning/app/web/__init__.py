from flask import Blueprint

web = Blueprint('web', __name__) #蓝图是为了拆分模块的, 也可以指定staticfolder和static url

from app.web import book
from app.web import user