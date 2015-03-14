import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))
from datetime import datetime

##########################
# Initializing Flask app #
##########################
from flask import Flask, render_template, request, flash, redirect, session, url_for, g
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__, static_folder='static', static_url_path='')
app.config['DEBUG'] = True
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'you-will-never-guess'

app.swgi_app = ProxyFix(app.wsgi_app)

##############################
# Start website redirections #
##############################
@app.route('/', methods = ['GET', 'POST'])
def index():
	return render_template('index.html')

