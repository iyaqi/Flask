from flask import render_template
from . import main

# 404
@main.app_errorhandler(404)
def page_no_found(e):
    return render_template('400.html'), 404


# 500

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500