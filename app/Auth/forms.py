from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField,SubmitField, PasswordField
from wtforms.validators import DataRequired,Length,Email


class LoginForm(FlaskForm):
    email = StringField(id='Email'
                           ,label="邮箱",
                           validators=[
                                DataRequired(),
                                Length(1,64),
                                Email()
                                 ]
                           )
    password = PasswordField(id='password',
                             label="密码",
                             validators=[
                                 DataRequired(),
                             ])
    remember_me = BooleanField(
        id='remember_me',
        label="记住账号",
        default=False)
    submit = SubmitField(
                        id='Sign',
                         label="登录"
    )
