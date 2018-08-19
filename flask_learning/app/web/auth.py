from . import web
from flask import render_template, request,redirect, url_for, flash
from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from app.models.user import User
from app.models.base import db
from flask_login import login_user, logout_user

@web.route('/register', methods=['GET', 'POST']) #返回页面是get，用户提交是post
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)



@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email = form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True) #remembercookie duriation 默认设置是365天
            next = request.args.get('next') #登陆后跳转回之前页面
            if not  next or not next.startswith('/'): #防止非法next字符串 造成非法重定向
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或密码错误')

    return render_template('auth/login.html',)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == 'POST':
       if form.validate():
            account_email = form.email.data
            user = User.query.filter_by(email = account_email).first_or_404()
            #没有user，会抛出异常，不会执行后面代码，
            from app.libs.email import send_email
            send_email(form.email.data, 'Reset Your password', 'email/reset.html',
                       user=user, token=user.generate_token())
            flash('一封邮件已送达信箱' + account_email + '， 请及时查收')
            # return redirect(url_for('web.login'))
    return render_template("auth/forget_password_request.html", form = form)


#单元测试，解决测试过程过于冗长的问题


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    form = ResetPasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        success = User.reset_password(token, form.password1.data)
        if success:
            flash("Reset Sccessully")
            return redirect(url_for('web.login'))
        else:
            flash("Fail")
    return render_template('auth/forget_password.html', form=form)


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    logout_user() #清空浏览器cookie
    return redirect(url_for('web.indx'))


#可调用对象，需要实现————call————函数，将对象当作函数使用
#模糊了对象和函数区别，统一调用接口
