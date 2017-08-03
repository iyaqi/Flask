from datetime import datetime

from flask import render_template

from . import main


# index

@main.route('/')
@main.route('/index',methods =['GET','POST'])
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

