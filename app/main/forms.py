from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField,SubmitField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    userName = StringField(id='userName',label="用户名", validators=[DataRequired(), ])
    password = PasswordField(id='password',label="密码",validators=[DataRequired(),])
    remember_me = BooleanField(id='remember_me',label="记住账号", default=False)
    submit = SubmitField(id='Sign',label="登录")
