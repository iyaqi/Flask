from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User', backref = 'role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True) # id

    name = db.Column(db.String,index=True) #名称

    email = db.Column(db.String) # 邮箱

    password_hash = db.Column(db.String) # 密码

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) # 角色

    confirmed = db.Column(db.Boolean,default=False)

    # 秒数方法
    def __repr__(self):
        return '<User %r>' % self.name

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute!')

    # 设置密码的 setter方法
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    # 验证密码
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)



    # 生成token
    def generate_confirmation_token(self,expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'],expiration)
        return s.dumps({'confirm':self.id})

    # 验证token

    def confirm(self,token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        print(data['confirm'],self.id)
        if data.get('confirm') != self.id :
            return False
        self.confirmed = True
        db.session.add(self)
        return  True

# 回调函数
@login_manager.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))