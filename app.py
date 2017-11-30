from flask import Flask, render_template, request, session, redirect, url_for
import pymysql
import sys
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)


# connect to database
conn = pymysql.connect(host='localhost', port=3306, user='root', password='password', db='cd-marketplace')
cur = conn.cursor()


# Functions to write
# Checks if user is on database. Used in login
def checkLogin(username, password):
	query = "SELECT * FROM users WHERE username LIKE '{}' AND password LIKE '{}'".format(username, password)
	print(bool(cur.execute(query)))
	if cur.execute(query):
		return True
	else:
		return False


# Check if username has a duplicate. Used for registration
def checkUser(username):
	query = "SELECT * FROM users WHERE username LIKE '{}'".format(username)
	print(bool(cur.execute(query)))
	if cur.execute(query):
		return True
	else:
		return False


# Check if email has a duplicate. Used for registration
def checkEmail(email):
	query = "SELECT * FROM users WHERE email LIKE '{}'".format(email)
	print(bool(cur.execute(query)))
	if cur.execute(query):
		return True
	else:
		return False


# Returns the userid and role of current user. Returns a tuple ex: (1, d)
def getUserIdRole(username):
	query = "SELECT user_id, role FROM users WHERE username LIKE '{}'".format(username)
	cur.execute(query)
	data = cur.fetchone()
	return data


# Routes
@app.route('/')
def home():
	print("Home page")
	return render_template("home.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if checkLogin(username, password):
			session['username'] = username  # this is a string
			session['user_id'] = getUserIdRole(username)[0]  # this is an int
			session['role'] = getUserIdRole(username)[1]  # this is a char 'd' or 'c'
			session['logged_in'] = True
			return redirect(url_for('home'))
		else:
			error = True
			return render_template("login.html", error=error)
	return render_template("login.html", error=error)


@app.route('/register', methods=['GET','POST'])
def register():
	print("Registration page")
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		conf_password = request.form['confirm-password']
		email = request.form['email']

		if (not checkUser(username)) and (not checkEmail(email)):
			return render_template("register.html", success=True)
		else:
			return render_template("register.html", user=True)

	else:
		return render_template("register.html")


@app.route('/profile')
def profile():
	username = session['username']
	return render_template("profile.html", name=username)


@app.route('/compose')
def compose():
	return render_template("compose.html")


@app.route('/admin')
def admin():
	return render_template("admin.html")


@app.route('/about')
def about():
	return render_template("about.html")


@app.route('/postings')
def postings():
	return render_template("postings.html")


@app.route('/signout')
def signout():
	session['logged_in'] = False
	return redirect(url_for('home'))


if __name__ == "__main__":
	app.run(debug=True)