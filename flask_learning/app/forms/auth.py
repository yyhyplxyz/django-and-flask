from wtforms import Form, StringField, IntegerField,PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, Email, ValidationError
from app.models.user import User
class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8,64), Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入密码'), Length(6,32)
    ])

    nickname = StringField(validators=[DataRequired(), Length(2,10,message='昵称至少需要两个字符，最多十个字符')])

    #自定义验证器
    def validate_email(self,field):
        if User.query.filter(email=field.data).first():
            raise ValidationError('电子邮箱已被注册')

    def validate_nickname(self, field):
        if User.query.filter(email=field.data).first():
            raise ValidationError('用户已被注册')


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8,64), Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入密码'), Length(6,32)
    ])

    nickname = StringField(validators=[DataRequired(), Length(2,10,message='昵称至少需要两个字符，最多十个字符')])


