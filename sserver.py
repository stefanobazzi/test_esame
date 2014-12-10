#! /usr/bin/env python
# -*- unicode:utf-8 -*-

from flask import Flask, request, Response, render_template, flash, redirect, url_for
from functools import wraps
import os.path

app = Flask(__name__)
app.secret_key = 'pippo'
user_dir = os.path.dirname(os.path.realpath(__file__))
users = {}

def check_user(user, pwd):
	return USER == user and PWD == pwd


class User(object):

	def __init__(self, name=None, pwd=None):
		self.name = name
		self.pwd = pwd

user = User()

def hello():
	return "hello"

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		if request.form['name'] != app.config['USERNAME'] or
			request.form['pwd'] != app.config['PASSWORD']:
				error = 'Invalid username/password'
		else:
			session['logged_in'] = True
			flash('Logged!')

	return render_template('login.html', error=error)

if __name__ == "__main__":
	app.run(debug=True)
