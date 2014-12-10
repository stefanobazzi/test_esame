from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route("/hello")
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
