from flask import Flask, render_template, request, session, redirect, url_for
import pymysql
import sys
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)


# connect to database
conn = pymysql.connect(host='localhost', port=3306, user='root', password='password', db='cd-marketplace', autocommit=True)
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


# TODO: Check if the email is on blacklist
# Check if email has a duplicate. Used for registration
def checkEmail(email):
	query = "SELECT * FROM users WHERE email LIKE '{}'".format(email)
	print(bool(cur.execute(query)))
	if cur.execute(query):
		return True
	else:
		return False


# Returns the userid and role of current user. Returns a tuple ex: (1, d)
def getUser(username):
	query = "SELECT user_id, email, role, first_name, last_name, rating, warning, description, confirmed FROM users WHERE username LIKE '{}'".format(username)
	cur.execute(query)
	data = cur.fetchone()
	return data


# Insert new_user to the database
def registerUser(username, email, password, role, first_name, last_name):
	query = "INSERT INTO users (username, email, password, role, first_name, last_name) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(username, email, password, role, first_name, last_name)
	cur.execute(query)
	print("Inserted to database successfully")
	return True


# Routes
@app.route('/')
def home():
	print("Home page")
	return render_template("home.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
	# TODO: Check if the email is on blacklist
	error = None
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if checkLogin(username, password):
			session['username'] = username
			session['user_id'] = getUser(username)[0]
			session['email'] = getUser(username)[1]
			session['role'] = getUser(username)[2]
			session['first_name'] = getUser(username)[3]
			session['last_name'] = getUser(username)[4]
			session['rating'] = getUser(username)[5]
			session['warning'] = getUser(username)[6]
			session['description'] = getUser(username)[7]
			session['confirmed'] = getUser(username)[8]
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
		first_name = request.form['first_name']
		last_name = request.form['last_name']
		username = request.form['username']
		password = request.form['password']
		conf_password = request.form['confirm-password']
		email = request.form['email']
		role = request.form['role']

		if password == conf_password:
			# If username and email are not on the database, register the user to new_users
			if (not checkUser(username)) and (not checkEmail(email)):
				registerUser(username, email, password, role, first_name, last_name)
				return render_template("register.html", success=True)
			else:
				return render_template("register.html", user=True)
		else:
			return render_template("register.html", password=True)

	else:
		return render_template("register.html")


@app.route('/profile')
def profile():
	role = 'Client'
	# BUG
	if session['confirmed'] != 0:
		confirmed_user = True
	elif session['confirmed'] == 0:
		confirmed_user = False
	if session['role'] == 'd':
		role = 'Developer'
	return render_template("profile.html", confirmed=confirmed_user, role=role)
	# For accepted applicant, they need to be greeted to


@app.route('/compose')
def compose():
	return render_template("compose.html")


# TODO: Admins login on the login page with the role of 'a'
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


## BLACKLIST: unban user after 1 year.

## THE DEveloper cannot post, the client can post

## TOP 3 clients and developers are shown in web page

	# username = session['username']
	# user_id = session['user_id']
	# email = session['email']
	# role = session['role']
	# first_name = session['first_name']
	# last_name = session['last_name']
	# rating = session['rating']
	# warning = session['warning']
	# description = session['description']
	# confirmed = session['confirmed']