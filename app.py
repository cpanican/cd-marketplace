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
	query = "SELECT user_id, email, role, first_name, last_name, rating, warning, description, confirmed, finished_projects, interest, sample_work, business_credential, balance FROM users WHERE username LIKE '{}'".format(username)
	cur.execute(query)
	data = cur.fetchone()
	return data


def getUserById(user_id):
	query = "SELECT * FROM users WHERE user_id = {}".format(user_id)
	cur.execute(query)
	data = cur.fetchone()
	return data

# Return True if user in blacklist
def getBlacklist(username):
	query = "SELECT reason, date FROM blacklist JOIN users ON blacklist.user_id = users.user_id WHERE username LIKE '{}'".format(username)
	if cur.execute(query):
		data = cur.fetchone()
		print(data)
		print("user is in the blacklist")
		return data
	else:
		print("user is not in the blacklist")
		return


# Insert new_user to the database
def registerUser(username, email, password, role, first_name, last_name):
	query = "INSERT INTO users (username, email, password, role, first_name, last_name) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(username, email, password, role, first_name, last_name)
	cur.execute(query)
	print("Inserted to users database successfully")
	return True

def editProfile(user_id, description, interest, resume, sample_work, business_credential):
	if description:
		query = "UPDATE users SET description = '{}' WHERE user_id = {}".format(description, user_id)
		print(query)
		cur.execute(query)
	if interest:
		query = "UPDATE users SET interest = '{}' WHERE user_id = {}".format(interest, user_id)
		print(query)
		cur.execute(query)
	if resume:
		query = "UPDATE users SET resume = '{}' WHERE user_id = {}".format(resume, user_id)
		print(query)
		cur.execute(query)
	if sample_work:
		query = "UPDATE users SET sample_work = '{}' WHERE user_id = {}".format(sample_work, user_id)
		print(query)
		cur.execute(query)
	if business_credential:
		query = "UPDATE users SET business_credential = '{}' WHERE user_id = {}".format(business_credential, user_id)
		print(query)
		cur.execute(query)
	print("Updated users database successfully")
	return True

#################################### FUNCTIONS FOR POSTINGS ######################################################
#################################################### BUG ON CURR_PRICE #########################################################
# # Post a bid and write it on the database
def postBid(title, description, start_price, deadline, file, visibility, user_id):
	query = "INSERT INTO post (title, proj_description, start_price, file, visibility, client_id, project_days) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(title, description, start_price, file, visibility, user_id, deadline)
	print(query)
	cur.execute(query)
	print(type(deadline))
	query2 = "UPDATE post SET deadline = DATE_ADD(deadline, INTERVAL 7 DAY)"
	print(query2)
	cur.execute(query2)
	print("Inserted to post database successfully")
	return True



# Show all posts newest first on postings page
def showPosts():
	query = "SELECT job_id, proj_description, start_price, deadline, post_date, dev_id, client_id, title, file, visibility, project_days, email, username, first_name, last_name, bids, clicks FROM post JOIN users ON post.client_id = users.user_id ORDER BY post_date DESC"
	cur.execute(query)
	data = cur.fetchall()
	return data


# Show one specific post
def showOnePost(job_id):
	query = "SELECT job_id, proj_description, start_price, deadline, post_date, dev_id, client_id, title, file, visibility, project_days, email, username, first_name, last_name, bids, clicks FROM post JOIN users ON post.client_id = users.user_id WHERE job_id = {}".format(job_id)
	cur.execute(query)
	data = cur.fetchone()
	return data


# Show post with title as parameter
def showLatestPostByClient(client_id):
	query = "SELECT job_id, proj_description, start_price, deadline, post_date, dev_id, client_id, title, file, visibility, project_days, email, username, first_name, last_name, bids, clicks FROM post JOIN users ON post.client_id = users.user_id WHERE client_id = 2 ORDER BY post_date DESC LIMIT 1;"
	cur.execute(query)
	data = cur.fetchone()
	return data


# Show developer bidders on specific project
def showPostBids(job_id):
	query = "SELECT job_id, dev_id, price, date, username, first_name, last_name FROM bids JOIN users ON bids.dev_id = users.user_id WHERE job_id = {} ORDER BY date DESC".format(job_id)
	cur.execute(query)
	data = cur.fetchall()
	return data


def appendClicks(job_id):
	# Append clicks
	query = "UPDATE post SET clicks = clicks + 1 WHERE job_id = {}".format(job_id)
	cur.execute(query)
	print("Click appended")
	return True


def newBid(job_id, dev_id, price):
	query = "INSERT INTO bids (job_id, dev_id, price) VALUES ({}, {}, {})".format(job_id, dev_id, price)
	cur.execute(query)
	print("Bid updated")
	return True


def incrementBid(job_id):
	query = "UPDATE post SET bids = bids + 1 WHERE job_id = {}".format(job_id)
	cur.execute(query)
	print("Bids appended")
	return True


def top3Bids():
	query = "SELECT * from post ORDER BY clicks DESC LIMIT 3"
	cur.execute(query)
	data = cur.fetchall()
	print("Top 3 bids loaded")
	print(data)
	return data

def top3Devs():
	query = "SELECT * from users WHERE role = 'd' AND confirmed = 1 ORDER BY rating DESC LIMIT 3"
	cur.execute(query)
	data = cur.fetchall()
	print("Top 3 developers loaded")
	print(data)
	return data


def top3Clients():
	query = "SELECT * from users WHERE role = 'c' AND confirmed = 1 ORDER BY rating DESC LIMIT 3"
	cur.execute(query)
	data = cur.fetchall()
	print("Top 3 clients loaded")
	print(data)
	return data


################################## ADMIN FUNCTIONS ############################################
# return all users in blacklist
def adminBlacklist():
	query = "SELECT * FROM users JOIN blacklist ON users.user_id = blacklist.user_id"
	cur.execute(query)
	data = cur.fetchall()
	print("All Blacklist loaded")
	print(data)
	return data

# Return all users not on blacklist
def adminUsers():
	query = "SELECT * FROM users WHERE NOT EXISTS (SELECT user_id FROM blacklist WHERE users.user_id = blacklist.user_id)"
	cur.execute(query)
	data = cur.fetchall()
	print("All Users not on blacklist loaded")
	print(data)
	return data

# Return unconfirmed users
def adminUnconfirmed():
	query = "SELECT * FROM users WHERE NOT EXISTS (SELECT user_id FROM blacklist WHERE users.user_id = blacklist.user_id) AND confirmed = 0 AND role != 'a'"
	cur.execute(query)
	data = cur.fetchall()
	print("All unconfirmed users loaded")
	print(data)
	return data

# Return projects with reports
def adminProjReport():
	query = "SELECT * FROM project WHERE client_rating < 3"
	cur.execute(query)
	data = cur.fetchall()
	print("All reported projects loaded")
	print(data)
	return data


# Return users in warning
def adminWarning():
	query = "SELECT * FROM users JOIN blacklist ON blacklist.user_id != users.user_id WHERE confirmed != 1 AND role != 'a' AND rating < 3 AND finished_projects >= 5"
	cur.execute(query)
	data = cur.fetchall()
	print("All warned users loaded")
	print(data)
	return data


# Set user as confirmed profile
def adminConfirmProfile(username):
	query = "UPDATE users SET confirmed = 1 WHERE username = '{}'".format(username)
	cur.execute(query)
	print(username + ' is now confirmed')
	return True


# Ban user from the system
def adminBanProfile(user_id, reason):
	query = "INSERT INTO blacklist (user_id, reason) VALUES ({}, '{}')".format(user_id, reason)
	cur.execute(query)
	print("user is successfully banned")
	return True


# Unban user from the system
def adminUnbanProfile(user_id):
	query = "DELETE FROM blacklist WHERE user_id = {}".format(user_id)
	cur.execute(query)
	print(user_id + ' has been unbanned')
	return True


##################### Function for deposit, withdraw, anything that involves money #############3######
# Deposit money on database
def depositMoney(username, amount):
	query = "UPDATE users SET balance = balance + {} WHERE username = '{}'".format(amount, username)
	cur.execute(query)
	print("deposit success")
	return True

# Withdraw money from your account
def withdrawaMoney(username, amount):
	query = "UPDATE users SET balance = balance - {} WHERE username = '{}'".format(amount, username)
	cur.execute(query)
	print("withdraw success")
	return True










# Routes
@app.route('/')
def home():
	print("Home page")
	if ('logged_in' in session) and (session['logged_in'] == True):
		print('You are logged in')
		session['logged_in'] = True
	else:
		print('You are not logged in')
		session['logged_in'] = False
	bids = top3Bids()
	devs = top3Devs()
	clients = top3Clients()
	return render_template("home.html", bids=bids, devs=devs, clients=clients)


@app.route('/login', methods=['GET', 'POST'])
def login():
	print("Login Page")
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
			session['finished_projects'] = getUser(username)[9]
			session['interest'] = getUser(username)[10]
			session['sample_work'] = getUser(username)[11]
			session['business_credential'] = getUser(username)[12]
			session['balance'] = getUser(username)[13]
			session['logged_in'] = True
			getBlacklist(username)
			if session['role'] != 'a':
				return redirect(url_for('dashboard'))
			else:
				return redirect(url_for('admin'))
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
			if (not checkUser(username)) and (not checkEmail(email)):
				registerUser(username, email, password, role, first_name, last_name)
				return render_template("register.html", success=True)
			else:
				return render_template("register.html", user=True)
		else:
			return render_template("register.html", password=True)

	else:
		return render_template("register.html")


@app.route('/dashboard')
def dashboard():
	isValidUser=False
	if session['logged_in']:
		isValidUser = True
		if session['role'] == 'd':
			role = 'Developer'
		elif session['role'] == 'c':
			role = 'Client'
		elif session['role'] == 'a':
			role = 'Admin'
		print(session['confirmed'])
		if session['confirmed'] != 0:
			confirmed_user = True
		elif session['confirmed'] == 0:
			confirmed_user = False

		session['description'] = getUser(session['username'])[7]
		session['confirmed'] = getUser(session['username'])[8]
		session['finished_projects'] = getUser(session['username'])[9]
		session['interest'] = getUser(session['username'])[10]
		session['sample_work'] = getUser(session['username'])[11]
		session['business_credential'] = getUser(session['username'])[12]
		session['balance'] = getUser(session['username'])[13]

		print(confirmed_user)
		if role == 'Client':
			return render_template("dashboard.html", confirmed=confirmed_user, isValidUser=isValidUser, role=role, client=True)
		if role == 'Developer':
			return render_template("dashboard.html", confirmed=confirmed_user, isValidUser=isValidUser, role=role, developer=True)
		if role == 'Developer':
			return render_template("dashboard.html", confirmed=confirmed_user, isValidUser=isValidUser, role=role, admin=True)
	else:
		return render_template("dashboard.html", isValidUser=False)


@app.route('/profile')
def profile_redirect():
	print("Profile Redirect")
	return redirect(url_for('profile', username=session['username']))


@app.route('/profile/<username>', methods=['GET'])
def profile(username):
	email = getUser(username)[1]
	role = getUser(username)[2]
	first_name = getUser(username)[3]
	last_name = getUser(username)[4]
	rating = getUser(username)[5]
	warning = getUser(username)[6]
	description = getUser(username)[7]
	confirmed = getUser(username)[8]
	finished_projects = getUser(username)[9]
	interest = getUser(username)[10]
	sample_work = getUser(username)[11]
	business_credential = getUser(username)[12]
	if confirmed != 0:
		confirmed_user = True
	elif confirmed == 0:
		confirmed_user = False

	if role == 'd':
		role = 'Developer'
	if role == 'c':
		role = 'Client'
	elif role == 'a':
		role = 'Admin'

	return render_template("profile.html", email=email, role=role, first_name=first_name, last_name=last_name, rating=rating, warning=warning, description=description, confirmed=confirmed_user, finished_projects=finished_projects, interest=interest, sample_work=sample_work, business_credential=business_credential)
	# For accepted applicant, they need to be greeted to a edit resume page etc.
	# Blacklist user should show when they were banned reason and how many days left:


@app.route('/compose', methods=['GET','POST'])
def compose():
	print("Compose Page")
	error = None
	if request.method == 'POST':
		title = request.form['title']
		description = request.form['description']
		start_price = request.form['start_price']
		deadline = request.form['deadline']
		file = request.form['file']
		visibility = int(request.form['visibility'])
		user_id = session['user_id']
		description = description.replace("'", "''")
		title = title.replace("'", "''")
		print(type(description))
		print(type(file))
		print(title)
		print(description)
		print(start_price)
		print(deadline)
		print(file)
		print(visibility)
		print(user_id)
		if postBid(title, description, start_price, deadline, file, visibility, user_id):
			# Get the job_id and return a template
			posting = showLatestPostByClient(session['user_id'])
			return render_template("post.html", post=posting)
		else:
			error = True
			return render_template("compose.html", error=error)
	else:
		return render_template("compose.html")


@app.route('/admin')
def admin():
	unconfirmed_users = adminUnconfirmed()
	proj_reports = adminProjReport()
	warn_users = adminWarning()
	return render_template("admin.html", unconfirmed=unconfirmed_users, reports=proj_reports, warns=warn_users)


# Admin function: accept user
@app.route('/admin/accept-user/<username>', methods=['GET', 'POST'])
def admin_accept(username):
	if session['logged_in'] == True:
		if session['role'] == 'a':
			adminConfirmProfile(username)
			return redirect(url_for('admin'))
		else:
			return redirect(url_for('admin_users'))
	else:
		return redirect(url_for('admin_users'))


# Admin function: ban user
@app.route('/admin/ban/<username>', methods=['GET', 'POST'])
def admin_ban(username):
	if session['logged_in'] == True:
		if session['role'] == 'a':
			ban_user_id = getUser(username)[0]
			if request.method == 'POST':
				reason = request.form['reason']
				adminBanProfile(ban_user_id, reason)
				return redirect(url_for('admin_users'))
			else: 
				return render_template('ban.html', user_id=ban_user_id, username=username)
		else:
			return redirect(url_for('admin'))
	else:
		return redirect(url_for('admin'))


@app.route('/admin-users')
def admin_users():
	blacklist = adminBlacklist()
	all_users = adminUsers()
	return render_template("admin-users.html", blacklist=blacklist, users=all_users)


@app.route('/admin-users/unban/<user_id>')
def admin_unban(user_id):
	if session['logged_in'] == True:
		if session['role'] == 'a':
			adminUnbanProfile(user_id)
			return redirect(url_for('admin_users'))
		else:
			return redirect(url_for('admin_users'))
	else:
		return redirect(url_for('admin_users'))


@app.route('/about')
def about():
	return render_template("about.html")


# postings/project-name
@app.route('/posting')
def postings():
	posts = showPosts()
	#job_id, proj_description, start_price, deadline, post_date, dev_id, client_id, title, curr_price, file, visibility, project_days, email, username, first_name, last_name, bids
	return render_template("postings.html", posts=posts)


@app.route('/posting/<job_id>', methods=['GET', 'POST'])
def post(job_id):
	post = showOnePost(job_id)
	bids = showPostBids(job_id)
	appendClicks(job_id)
	if request.method == 'POST':
		if session['role'] == 'c':
			return render_template("post.html", post=post, bids=bids, client=True)
		else:
			price = request.form['bid']
			dev_id = session['user_id']
			newBid(job_id, dev_id, price)
			incrementBid(job_id)
			bids = showPostBids(job_id)
			return render_template("post.html", post=post, bids=bids, success=True)
	else:
		return render_template("post.html", post=post, bids=bids)


@app.route('/edit-profile' , methods=['GET','POST'])
def edit_profile():
	print("edit-profile Page")
	error = None
	if request.method == 'POST':
		description = request.form['description']
		interest = request.form['interest']
		resume = request.form['resume']
		sample_work = request.form['sample_work']
		business_credential = request.form['business_credential']
		description = description.replace("'", "''")
		interest = interest.replace("'", "''")
		sample_work = sample_work.replace("'", "''")
		business_credential = business_credential.replace("'", "''")
		user_id = session['user_id']
		editProfile(user_id, description, interest, resume, sample_work, business_credential)
		return redirect(url_for("dashboard"))
	return render_template("edit-profile.html")


@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
	# if method post redirect to dashboard
	print('deposit')
	if request.method == 'POST':
		amount = request.form['balance']
		username = request.form['username']
		print(amount)
		print(username)
		depositMoney(username, amount)
		return redirect(url_for("dashboard"))
	return render_template("deposit.html")


@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
	# if method post redirect to dashboard
	if request.method == 'POST':
		amount = request.form['balance']
		username = request.form['username']
		withdrawMoney(username, amount)
		return redirect(url_for("dashboard"))
	return render_template("withdraw.html")


@app.route('/signout')
def signout():
	session['logged_in'] = False
	session.clear()
	return redirect(url_for('home'))


if __name__ == "__main__":
	app.run(debug=True)


## BLACKLIST: unban user after 1 year.


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
