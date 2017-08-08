from datetime import datetime
from flask import render_template

from . import main


# index

@main.route('/')
@main.route('/index',methods =['GET','POST'])
def index():
    return render_template("index.html")

# About

@main.route('/about',endpoint='about')
def about():
    user = {'nikeName': 'Dodge'}
    print(datetime.now())
    return render_template("about.html",
                           user=user,
                           current_time = datetime.utcnow()
                           )

