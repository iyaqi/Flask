from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField,SubmitField, PasswordField
from wtforms.validators import DataRequired,Length,Email,EqualTo,Regexp

# 登录
class LoginForm(FlaskForm):
    email = StringField(id='Email',label="邮箱",
                        validators=[
                            DataRequired(),
                            Length(1,64),
                            Email()
                        ])
    password = PasswordField(id='password',label="密码",validators=[DataRequired(),])
    remember_me = BooleanField(id='remember_me',label="记住账号",default=False)
    submit = SubmitField(id='Sign',label="登录")



# 注册
class RegisterForm(FlaskForm):

    email = StringField(
        id='email', label="邮箱",
        validators=[
            DataRequired(),
            Length(1, 64),
            Email()
        ]
    )
    name = StringField(
        id='name',
        label="用户名",
        validators=[
            DataRequired(),
            Length(1,64),
            Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,message='名称必须是字母、数组、下划线'
                                                        '或者.')
        ]
    )
    password = PasswordField(
        id='password',
        label="密码",
        validators=[
            DataRequired(),
            EqualTo('check_password',message='密码必须相同')
        ]
    )
    check_password = PasswordField(
        id='check_password',
        label="确认密码",
        validators=[
            DataRequired(),
        ]
    )
    submit = SubmitField(
        id='sign',
        label="注册"
    )

class ResetPasswordForm(FlaskForm):
    password = PasswordField(
        id='password',
        label="旧密码",
        validators=[
            DataRequired(),
        ]
    )
    new_password1 = PasswordField(
        id='password1',
        label="新密码",
        validators=[
            DataRequired(),
        ]
    )
    new_password2 = PasswordField(
        id='password2',
        label="重复新密码",
        validators=[
            DataRequired(),
            EqualTo('password1',message='新密码不一致!')
        ]
    )
    submit = SubmitField(
        id='save',
        label="修改"
    )