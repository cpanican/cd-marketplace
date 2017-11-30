from flask import Flask, render_template, request, session, redirect, url_for, flash
import pymysql
import sys

app = Flask(__name__)
app.secret_key = 'super secret key'

# connect to database
conn = pymysql.connect(host='localhost', port=3306, user='root', password='password', db='cd-marketplace')
cur = conn.cursor()


# Functions to write
#
#




# Routes
@app.route('/')
def home():
	print("Home page")
	return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		session['logged_in'] = True
		flash('You were logged in')
		return redirect(url_for('home'))
	return render_template("login.html", error=error)

@app.route('/register', methods=['GET','POST'])
def register():
	print("Registration page")
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		conf_password = request.form['confirm-password']
		email = request.form['email']

		print(username)
		print(password)
		print(conf_password)
		print(email)

		confirmation = True
		return render_template("register.html", success=confirmation)
	else:
		return render_template("register.html")

@app.route('/profile')
def profile():
	username = ""
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