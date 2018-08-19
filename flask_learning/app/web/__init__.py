from flask import Blueprint, render_template

web = Blueprint('web', __name__) #蓝图是为了拆分模块的, 也可以指定staticfolder和static url

@web.app_errorhandler(404)
def not_found():
    #AOP思想，面向切片编程，所有404都在这里处理
    return render_template('404.html')

from app.web import book
from app.web import user
from app.web import auth
from app.web import gift
from app.web import  wish
from app.web import drift
from app.web import main