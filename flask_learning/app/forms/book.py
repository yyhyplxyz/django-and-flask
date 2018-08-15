from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired
class searchform(Form):
    q = StringField(validators=[DataRequired(message='只是空格'),Length(min=1,max=30,message='长度错误')]) #自定义报错信息
    page = IntegerField(validators=[NumberRange(min=1,max=99)], default=1)