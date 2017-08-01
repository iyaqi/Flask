from datetime import datetime

from flask import redirect, render_template,session

from . import main
from .forms import LoginForm
from ..models import User,Role
from .. import db

# index

@main.route('/',methods =['GET','POST'])
def index():
    user = {'nikeName': 'Dodge'}
    posts = [
        {
            'author': 'Shawn',
            'Content': 'dasdsajkdhakjsdhk'
        },
        {
            'author': 'Beck',
            'Content': 'dasdsajkdhakjsdhk'
        },
        {
            'author': 'Andrea',
            'Content': 'dasdsajkdhakjsdhk'
        },
        {
            'author': 'Mason',
            'Content': 'dasdsajkdhakjsdhk'
        },
        {
            'author': 'Ken',
            'Content': 'dasdsajkdhakjsdhk'
        }
    ]
    return render_template("index.html",
                           user=user,
                           posts=posts,
                           )

# About


@main.route('/about',endpoint='about')
def about():
    user = {'nikeName': 'Dodge'}
    print(datetime.now())
    msg = Message('test subject',sender='ls_xyq@126.com')
    msg.body = 'test body'
    msg.html = '<b>Welcome you !</b>'
    with app.app_context():
        mail.send(msg)

    return render_template("about.html",
                           user=user,
                           current_time = datetime.utcnow()
                           )

# login


@main.route('/login', methods=['GET', 'POST'])
def login():
    if form.validate_on_submit():
        form = LoginForm()
        user = User.query.filter_by(username=form.userName.data).first()
        # if user is None:
        #     user = User(username = form.userName.data)
        #     db.session.add(user)
        #     session['known'] = False
        # else:
        #     session['known'] = True
        # session['name'] = form.userName.data
        return redirect(url_for('.index'))
    return render_template('login.html',
                           form=form,
                           name = session.get('name')
                           # known = session.get('known',False),
                           # current_time = datetime.utcnow()
                           )



