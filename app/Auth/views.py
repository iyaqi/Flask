from flask import render_template,redirect,request,url_for,flash
from flask_login import login_user,logout_user,login_required,current_user

from . import auth
from .forms import LoginForm,RegisterForm,ResetPasswordForm
from ..models import User
from .. import db
from ..mail import send_email


@auth.before_app_request
def before_request():
    if current_user.is_authenticated \
            and not current_user.confirmed \
            and request.endpoint \
            and request.endpoint[:5] != 'auth.' :
        return redirect(url_for('auth.unconfirmed'))

# 登录
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invaild email or password!')
    return render_template('auth/login.html',
                           form=form,
                           )
# 退出登录
@auth.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out!')
    return redirect(url_for('auth.login'))

# 注册
@auth.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,name=form.name.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_tolen()
        send_email(
            user.email,
            'Confirm your account','auth/email/confirm',
            user=user,
            token=token
        )
        flash('已给您的邮箱发送了邮件，请验证。')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',form = form)

# 验证邮箱
@auth.route('/confirm/<token>')
@login_required
def confirm(token):

    if current_user.confirmed:
        return redirect(url_for('main.index'))

    if current_user.confirm(token):
        flash('恭喜你通过验证')
    else:
        flash('你的验证信息已过期')

    return redirect(url_for('main.index'))


@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm Your Account',
           'auth/email/confirm', user=current_user, token=token)
    flash('A new confirmation email has been sent to you by email.')
    return redirect(url_for('main.index'))


@auth.route('/unconfirmed')
def unconfirmed():
    # print(current_user.is_anonymous,current_user.confirmed)
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


@auth.route('/resetpassword')
def resetpassword():
    form = ResetPasswordForm()
    return render_template(
        'auth/resetpassword.html',
        form=form
    )

