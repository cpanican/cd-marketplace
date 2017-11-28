from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


conn = pymysql.connect(host='localhost', port=3306, user='root', password='password', db='cd-marketplace')
cur = conn.cursor()


# Connect to Database
#
#


# Functions to write
#
#




# Routes
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
	return render_template("login.html")

@app.route('/register')
def register():
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


if __name__ == "__main__":
    app.run(debug=True)