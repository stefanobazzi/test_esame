#! /usr/bin/env python
# -*- unicode:utf-8 -*-

from flask import Flask, request, Response, render_template, flash, redirect, url_for
from functools import wraps
from werkzeug import secure_filename
import os.path

users = {}
user_dir = os.path.dirname(os.path.realpath(__file__))
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
img = os.path.join(user_dir, 'img')

app = Flask(__name__)
app.secret_key = 'pippo'
app.config['UPLOAD_FOLDER'] = img

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

def allowed_file(filename):
	return'.' in filename and \
		filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file(filename=None):
	if request.method == 'POST':
		f = request.files['file']
		if f and allowed_file(f.filename):
			filename = secure_filename(f.filename)
			f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	return render_template('upload.html')


@app.route('/home')
def home():
	return 'Hello %s' % user.name

@app.route('/share', methods=['GET'])
def share_img(filename):
	print url_for('img', filename=filename)

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
	if not os.path.exists('img'):
		os.makedirs(os.path.join(img))
	load_users()
	app.run(debug=True)
