import datetime
from flask import request, redirect, url_for, render_template, flash, abort, Flask
from flask_peewee.utils import get_object_or_404, object_list

from functools import wraps
from flask import request, Response

from utils.utils import json_response
from controller.logic import load_data

app = Flask(__name__)

@app.route('/')
def home():
	auth = request.authorization
	if auth.username != 'admin' or auth.password != 'thesecret': 
		abort(401)
	return json_response({
        'username': auth.username,
        'password': auth.password,
        'status': 'OK'
	})

@app.route('/upload')
def uploaddata():
	auth = request.authorization
	if auth.username != 'admin' or auth.password != 'thesecret' :
		abort(401)
	directory = request.args.get('dir')
	print("Loading data...")
	load_data(directory)
	return json_response({
        'directory': directory,
        'status': 'OK'
	})

@app.errorhandler(404)
def not_found(e):
    return json_response(status=404)