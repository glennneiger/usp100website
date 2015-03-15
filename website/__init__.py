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

##################
# Error Handlers #
##################
@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index')), 404

##############################
# Start website redirections #
##############################
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/1800s')
def eighteen():
	return render_template('1800s.html')

@app.route('/1900s')
def nineteen():
	return render_template('1900s.html')

@app.route('/2000s')
def twenty():
	return render_template('2000s.html')
