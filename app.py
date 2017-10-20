from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


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


if __name__ == "__main__":
    app.run(debug=True)