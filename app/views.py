import app
from flask_login import login_required
from flask import flash

@app.route('/secret')
@login_required
def secret():
    flash('Only authenticated users are allowed!')

