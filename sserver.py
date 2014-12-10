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


@app.route('/login', methods = ['GET', 'POST'])
def login():
	error = 'error'
	if request.method == 'POST':
		if not search_user(request.form['name'], request.form['pwd']):
				error = 'Invalid username/password'
		else:
			flash('Logged!')
			return redirect(url_for('home'))
	return render_template('login.html', error=error)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file(filename=None):
	if request.method == 'POST':
		f = request.files[filename]
		f.save(user_dir)


@app.route('/home')
def home():
	return 'Hello %s' % user.name


def search_user(name, pwd):
	found = False
	for k, v in users.items():
		if name == k and pwd == v:
			found = True
			user.name = k
			user.pwd = v
			break
	return found


def read_file(filename, charset='utf-8'):
    with open(filename, 'r') as f:
        return f.read().decode(charset)


def load_users():
	lines = read_file('settings').split('\n')
	for line in lines:
		k, v = line.split(' ')
		users[k] = v


if __name__ == "__main__":
	load_users()
	app.run(debug=True)
