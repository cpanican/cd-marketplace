import os

import pymysql
from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'somerandomtext'

# connect to database
# conn = pymysql.connect(host='localhost', port=3306, user='root', password='password', db='cd-marketplace',
#                        autocommit=True)
conn = pymysql.connect(host='us-cdbr-iron-east-05.cleardb.net', user='ba269511c15654', password='bafb1cdd',
                       db='heroku_13d3dee5aa34929', autocommit=True, connect_timeout=2147483)
cur = conn.cursor()


####################################### LOGIN REGISTER FUNCTIONS #######################################################
# Checks if user is on database. Used in login
def checkLogin(username, password):
    query1 = "SET SQL_SAFE_UPDATES = 0"
    cur.execute(query1)
    query = "SELECT * FROM users WHERE username LIKE '{}' AND password LIKE '{}'".format(username, password)
    if cur.execute(query):
        return True
    else:
        return False


# Check if username has a duplicate. Used for registration
def checkUser(username):
    query = "SELECT * FROM users WHERE username LIKE '{}'".format(username)
    if cur.execute(query):
        return True
    else:
        return False


# Check if email has a duplicate. Used for registration
def checkEmail(email):
    query = "SELECT * FROM users WHERE email LIKE '{}'".format(email)
    if cur.execute(query):
        return True
    else:
        return False


# Returns the userid and role of current user. Returns a tuple ex: (1, d)
def getUser(username):
    query = "SELECT user_id, email, role, first_name, last_name, rating, warning, description, confirmed, finished_projects, interest, sample_work, business_credential, balance FROM users WHERE username LIKE '{}'".format(
        username)
    cur.execute(query)
    data = cur.fetchone()
    return data


# Returns user with the user of user_id as input
def getUserById(user_id):
    query = "SELECT * FROM users WHERE user_id = {}".format(user_id)
    cur.execute(query)
    data = cur.fetchone()
    return data


# Return True if user in blacklist
def checkBlacklist(username):
    query = "SELECT reason, date FROM blacklist JOIN users ON blacklist.user_id = users.user_id WHERE username LIKE '{}'".format(
        username)
    if cur.execute(query):
        print("user is in the blacklist")
        return True
    else:
        print("user is not in the blacklist")
        return False


# Get all users in the blacklist
def getBlacklist(username):
    query = "SELECT reason, date FROM blacklist JOIN users ON blacklist.user_id = users.user_id WHERE username LIKE '{}'".format(
        username)
    cur.execute(query)
    data = cur.fetchone()
    print(data)
    return data


# Insert new_user to the database
def registerUser(username, email, password, role, first_name, last_name):
    query = "INSERT INTO users (username, email, password, role, first_name, last_name) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(
        username, email, password, role, first_name, last_name)
    cur.execute(query)
    print("Inserted to users database successfully")
    return True


# Edit profile page
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


############### FUNCTION FOR PROFILE PAGE (Active bids, Current Projects, and History Section #########################
# Show all active bids for developer
def showActiveBidsDev(user_id):
    query = "SELECT bids.job_id, start_price, price, title, project_days FROM bids JOIN post ON bids.job_id = post.job_id WHERE bids.dev_id = {} AND NOT EXISTS (SELECT job_id FROM project WHERE post.job_id = project.job_id)".format(
        user_id)
    cur.execute(query)
    data = cur.fetchall()
    return data


# Show all active bids for client
def showActiveBidsClient(user_id):
    query = "SELECT job_id, start_price, title, project_days FROM post WHERE client_id = {} AND NOT EXISTS (SELECT job_id FROM project WHERE post.job_id = project.job_id)".format(
        user_id)
    cur.execute(query)
    data = cur.fetchall()
    return data


# Show all current projects for developer
def showActiveProjectsDev(user_id):
    query = "SELECT project.job_id, title, project_days, status, final_price, deadline, post_date FROM project JOIN post ON project.job_id = post.job_id WHERE project.dev_id = {} AND (status = 'Ongoing' OR status = 'Pending')".format(
        user_id)
    cur.execute(query)
    data = cur.fetchall()
    return data


# Show all current projects
def showActiveProjectsClient(user_id):
    query = "SELECT project.job_id, title, project_days, status, final_price, deadline, post_date FROM project JOIN post ON project.job_id = post.job_id WHERE project.client_id = {} AND (status = 'Ongoing' OR status = 'Pending')".format(
        user_id)
    cur.execute(query)
    data = cur.fetchall()
    return data


# Show completed projects for dev
def showHistoryDev(user_id):
    query = "SELECT project.job_id, title, project_days, status, final_price FROM project JOIN post ON project.job_id = post.job_id WHERE project.dev_id = {} AND status = 'Completed'".format(
        user_id)
    cur.execute(query)
    data = cur.fetchall()
    return data


# Show completed projects for client
def showHistoryClient(user_id):
    query = "SELECT project.job_id, title, project_days, status, final_price FROM project JOIN post ON project.job_id = post.job_id WHERE project.client_id = {} AND status = 'Completed'".format(
        user_id)
    cur.execute(query)
    data = cur.fetchall()
    return data


#################################### FUNCTIONS FOR POSTINGS ######################################################
# # Post a bid and write it on the database
def postBid(title, description, start_price, deadline, file, visibility, user_id, budget):
    query1 = "SELECT * FROM users WHERE user_id = {} AND balance >= {}".format(user_id, budget)
    cur.execute(query1)
    if cur.rowcount:
        query = "INSERT INTO post (title, proj_description, start_price, file, visibility, client_id, project_days) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            title, description, start_price, file, visibility, user_id, deadline)
        cur.execute(query)
        query2 = "UPDATE post SET deadline = DATE_ADD(deadline, INTERVAL 7 DAY)"
        cur.execute(query2)
        print("Inserted to post database successfully")
        return True
    else:
        return False


# Show all posts newest first on postings page
def showPosts():
    query = "SELECT job_id, proj_description, start_price, date(deadline), post_date, dev_id, client_id, title, file, visibility, project_days, email, username, first_name, last_name, bids, clicks FROM post JOIN users ON post.client_id = users.user_id WHERE NOT EXISTS (SELECT job_id FROM project WHERE post.job_id = project.job_id) ORDER BY post_date DESC"
    cur.execute(query)
    data = cur.fetchall()
    return data


# Show one specific post
def showOnePost(job_id):
    query = "SELECT job_id, proj_description, start_price, deadline, post_date, dev_id, client_id, title, file, visibility, project_days, email, username, first_name, last_name, bids, clicks FROM post JOIN users ON post.client_id = users.user_id WHERE job_id = {}".format(
        job_id)
    cur.execute(query)
    data = cur.fetchone()
    return data


# Show post with title as parameter
def showLatestPostByClient(client_id):
    query = "SELECT job_id, proj_description, start_price, date(deadline), post_date, dev_id, client_id, title, file, visibility, project_days, email, username, first_name, last_name, bids, clicks FROM post JOIN users ON post.client_id = users.user_id WHERE client_id = {} ORDER BY post_date DESC LIMIT 1".format(
        client_id)
    cur.execute(query)
    data = cur.fetchone()
    return data


# Show developer bidders on specific project
def showPostBids(job_id):
    query = "SELECT job_id, dev_id, price, date, username, first_name, last_name FROM bids JOIN users ON bids.dev_id = users.user_id WHERE job_id = {} ORDER BY date DESC".format(
        job_id)
    cur.execute(query)
    data = cur.fetchall()
    return data


# Add one everytime someone visits a post
def appendClicks(job_id):
    # Append clicks
    query = "UPDATE post SET clicks = clicks + 1 WHERE job_id = {}".format(job_id)
    cur.execute(query)
    print("Click appended")
    return True


# submit a bid
def newBid(job_id, dev_id, price):
    query1 = "SELECT * FROM bids WHERE dev_id = {} AND job_id = {}".format(dev_id, job_id)
    if (cur.execute(query1)):
        query2 = "UPDATE bids SET price = {} WHERE job_id = {} AND dev_id = {}".format(price, job_id, dev_id)
        cur.execute(query2)
        print("Bid changed")
        return True
    else:
        query3 = "INSERT INTO bids (job_id, dev_id, price) VALUES ({}, {}, {})".format(job_id, dev_id, price)
        cur.execute(query3)
        print("Bid updated")
        return True


# Increment bid every time someone bids
def incrementBid(job_id):
    query = "UPDATE post SET bids = bids + 1 WHERE job_id = {}".format(job_id)
    cur.execute(query)
    print("Bids appended")
    return True


# Get top 3 bids
def top3Bids():
    query = "SELECT * from post WHERE NOT EXISTS (SELECT job_id FROM project WHERE post.job_id = project.job_id) ORDER BY clicks DESC LIMIT 3"
    cur.execute(query)
    data = cur.fetchall()
    print("Top 3 bids loaded")
    return data


# Get top 3 developers
def top3Devs():
    query = "SELECT * from users WHERE role = 'd' AND confirmed = 1 ORDER BY rating DESC LIMIT 3"
    cur.execute(query)
    data = cur.fetchall()
    print("Top 3 developers loaded")
    return data


# Get top 3 clients
def top3Clients():
    query = "SELECT * from users WHERE role = 'c' AND confirmed = 1 ORDER BY rating DESC LIMIT 3"
    cur.execute(query)
    data = cur.fetchall()
    print("Top 3 clients loaded")
    return data


################################## ADMIN FUNCTIONS ############################################
# return all users in blacklist
def adminBlacklist():
    query = "SELECT * FROM users JOIN blacklist ON users.user_id = blacklist.user_id"
    cur.execute(query)
    data = cur.fetchall()
    print("All Blacklist loaded")
    return data


# Return all users not on blacklist
def adminUsers():
    query = "SELECT * FROM users WHERE NOT EXISTS (SELECT user_id FROM blacklist WHERE users.user_id = blacklist.user_id)"
    cur.execute(query)
    data = cur.fetchall()
    print("All Users not on blacklist loaded")
    return data


# Return unconfirmed users
def adminUnconfirmed():
    query = "SELECT * FROM users WHERE NOT EXISTS (SELECT user_id FROM blacklist WHERE users.user_id = blacklist.user_id) AND confirmed = 0 AND role != 'a'"
    cur.execute(query)
    data = cur.fetchall()
    print("All unconfirmed users loaded")
    return data


# Return projects with reports
def adminProjReport():
    query = "SELECT project.job_id, title, dev_rating_desc, dev_rating FROM project JOIN post ON project.job_id = post.job_id WHERE status = 'Admin Review'"
    cur.execute(query)
    data = cur.fetchall()
    print("All reported projects loaded")
    return data


# Return users in warning
def adminWarning():
    query = "SELECT * FROM users WHERE confirmed != 0 AND role != 'a' AND rating < 15 AND finished_projects >= 5"
    cur.execute(query)
    data = cur.fetchall()
    print("All warned users loaded")
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


# Warn user
def adminWarnUser(username):
    query1 = "SET SQL_SAFE_UPDATES = 0"
    cur.execute(query1)
    query = "UPDATE users SET warning = warning + 1 WHERE username = '{}'".format(username)
    cur.execute(query)
    return True


# Take action for project complaints
def adminTakeAction(project_id, dev_rating, client_rating, old_dev_rating, old_client_rating, dev_id, client_id, percentage, price):
    query1 = "SET SQL_SAFE_UPDATES = 0"
    cur.execute(query1)
    query2 = "UPDATE project SET status = 'Completed', dev_rating = {}, client_rating = {} WHERE job_id = {}".format(
        dev_rating, client_rating, project_id)
    cur.execute(query2)
    query3 = "UPDATE users SET rating = rating - {} + {} WHERE user_id = {}".format(old_dev_rating, dev_rating, dev_id)
    cur.execute(query3)
    query4 = "UPDATE users SET rating = rating - {} + {} WHERE user_id = {}".format(old_client_rating, client_rating,
                                                                                    client_id)
    cur.execute(query4)

    # Calculate admin cut
    admin_cut = float(price) * 0.05
    remaining_price = float(price) - admin_cut

    # This amount is 100%
    half_price = float(remaining_price) / 2

    # Calculate percentage given to admin from input
    dev_pay = float(half_price) * (float(percentage)/100)
    client_pay = half_price - float(dev_pay)
    # Update dev Payment
    query5 = "UPDATE users SET balance = balance + {} WHERE user_id = {}".format(dev_pay, dev_id)
    cur.execute(query5)
    query6 = "UPDATE users SET balance = balance + {} WHERE user_id = {}".format(client_pay, client_id)
    cur.execute(query6)
    # Remove money from admin
    query7 = "UPDATE users SET balance = balance - {} WHERE user_id = 1".format(half_price)
    cur.execute(query7)
    return True


##################### Function for deposit, withdraw, anything that involves money #############3######
# Deposit money on database
def depositMoney(username, amount):
    query1 = "SET SQL_SAFE_UPDATES = 0"
    cur.execute(query1)
    query2 = "UPDATE users SET balance = balance + {} WHERE username = '{}'".format(amount, username)
    cur.execute(query2)
    print("deposit success")
    return True


# Withdraw money from your account
def withdrawMoney(username, amount):
    query1 = "SELECT * FROM users WHERE balance >= {} AND username = '{}'".format(amount, username)
    if cur.execute(query1):
        query2 = "SET SQL_SAFE_UPDATES = 0"
        cur.execute(query2)
        query3 = "UPDATE users SET balance = balance - {} WHERE username = '{}'".format(amount, username)
        cur.execute(query3)
        print("withdraw success")
        return True
    else:
        return False


#######################################################################################################
######################## Functions for project creation and submission #########################
# Return all projects (ongoing and pending)
def allProjects():
    query = "SELECT project.job_id, title, status, final_price, u1.first_name, u1.last_name, u2.first_name, u2.last_name FROM project JOIN users u1 ON project.dev_id = u1.user_id JOIN users u2 ON project.client_id = u2.user_id JOIN post ON project.job_id = post.job_id WHERE status = 'Ongoing' OR status = 'Pending'"
    cur.execute(query)
    data = cur.fetchall()
    return data


# Check if client has enough money to accept bid
def checkProjectBalance(client_id, price):
    query = "SELECT balance FROM users WHERE balance >= {} AND user_id = {}".format(price, client_id)
    if cur.execute(query):
        return True
    else:
        return False


# Create a project
def createProject(job_id, dev_id, client_id, price, project_days):
    query = "INSERT INTO project (job_id, status, final_price, dev_id, client_id) VALUES ({}, 'Ongoing', {}, {}, {})".format(
        job_id, price, dev_id, client_id)
    cur.execute(query)
    query1 = "UPDATE post SET dev_id = {} WHERE job_id = {}".format(dev_id, job_id)
    cur.execute(query1)
    query2 = "SET SQL_SAFE_UPDATES = 0"
    cur.execute(query2)
    query3 = "UPDATE project SET due_date = DATE_ADD(due_date, INTERVAL {} DAY) WHERE job_id = {}".format(project_days,
                                                                                                          job_id)
    cur.execute(query3)
    # Calculate admin cut
    admin_cut = float(price) * 0.05
    remaining_price = float(price) - admin_cut
    # Give have of balance to developer
    half_price = float(remaining_price) / 2
    query4 = "UPDATE users SET balance = balance + {} WHERE user_id = {}".format(half_price, dev_id)
    cur.execute(query4)
    query5 = "UPDATE users SET balance = balance - {} WHERE user_id = {}".format(price, client_id)
    cur.execute(query5)
    query6 = "UPDATE users SET balance = balance + {} + {} WHERE user_id = 1".format(admin_cut, half_price)
    cur.execute(query6)
    print("project created")
    return True


# Return project information with job_id
def findProject(job_id):
    query = "SELECT * FROM project WHERE job_id = {}".format(job_id)
    cur.execute(query)
    data = cur.fetchone()
    return data


# Return project information but with a developer
def findProjectAndDev(job_id):
    query = "SELECT job_id, status, final_price, dev_id, client_id, dev_rating_desc, client_id, submit_text, submit_file, user_id, username, first_name, last_name, client_rating_desc, dev_rating, client_rating FROM project JOIN users ON project.dev_id = users.user_id WHERE job_id = {}".format(
        job_id)
    cur.execute(query)
    data = cur.fetchone()
    return data


# Return due date of a project
def findProjectDueDate(job_id):
    query = "SELECT job_id, create_time, due_date FROM project WHERE job_id = {}".format(job_id)
    cur.execute(query)
    data = cur.fetchone()
    return data


# Used for project submission
def submitProject(job_id, dev_id, description, file):
    query1 = "SET SQL_SAFE_UPDATES = 0"
    cur.execute(query1)
    query2 = "UPDATE project SET status = 'Pending', submit_text = '{}', submit_file = '{}' WHERE job_id = {}".format(
        description, file, job_id)
    cur.execute(query2)
    return True


# From client to developer review
def giveProjectReviewForDeveloper(job_id, user_id, description, rating, status):
    query1 = "SET SQL_SAFE_UPDATES = 0"
    cur.execute(query1)
    query2 = "UPDATE project SET status = '{}', dev_rating = {}, dev_rating_desc = '{}' WHERE job_id = {}".format(
        status, rating, description, job_id)
    cur.execute(query2)
    query3 = "UPDATE users SET rating = rating + {}, finished_projects = finished_projects + 1 WHERE user_id = {}".format(
        rating, user_id)
    cur.execute(query3)
    return True


# Used for transferring remaining balance from admin to developer
def developerTransferRemaining(job_id, user_id):
    final_price = findProject(job_id)[2]
    admin_cut = float(final_price) * 0.05
    price_after_cut = float(final_price) - admin_cut
    remaining_balance = float(price_after_cut) / 2
    query1 = "UPDATE users SET balance = balance - {} WHERE user_id = 1".format(remaining_balance)
    cur.execute(query1)
    query2 = "UPDATE users SET balance = balance + {} WHERE user_id = {}".format(remaining_balance, user_id)
    cur.execute(query2)
    return True


# From developer to client review
def giveProjectReviewForClient(job_id, user_id, description, rating):
    query1 = "SET SQL_SAFE_UPDATES = 0"
    cur.execute(query1)
    query2 = "UPDATE project SET client_rating = {}, client_rating_desc = '{}' WHERE job_id = {}".format(rating,
                                                                                                         description,
                                                                                                         job_id)
    cur.execute(query2)
    query3 = "UPDATE users SET rating = rating + {}, finished_projects = finished_projects + 1 WHERE user_id = {}".format(
        rating, user_id)
    cur.execute(query3)
    return True


# Searching for Postings
def postSearch(search_input):
    query = "SELECT job_id, proj_description, start_price, date(deadline), post_date, dev_id, client_id, title, file, visibility, project_days, email, username, first_name, last_name, bids, clicks FROM post JOIN users ON post.client_id = users.user_id WHERE NOT EXISTS (SELECT job_id FROM project WHERE post.job_id = project.job_id) AND title LIKE '%{}%' ORDER BY post_date DESC".format(search_input)
    cur.execute(query)
    data = cur.fetchall()
    return data


# Searching for Projects
def projectSearch(search_input):
    query = "SELECT project.job_id, title, status, final_price, u1.first_name, u1.last_name, u2.first_name, u2.last_name FROM project JOIN users u1 ON project.dev_id = u1.user_id JOIN users u2 ON project.client_id = u2.user_id JOIN post ON project.job_id = post.job_id WHERE status = 'Ongoing' OR status = 'Pending' AND title LIKE '%{}%'".format(search_input)
    cur.execute(query)
    data = cur.fetchall()
    return data


# Searching for users
def userSearch(username, first_name, last_name, interest):
    query = "SELECT * FROM users WHERE username LIKE '%{}%' OR first_name LIKE '%{}%' OR last_name LIKE '%{}%' OR interest LIKE '%{}%'".format(username, first_name, last_name, interest)
    cur.execute(query)
    data = cur.fetchall()
    return data


# Grand Website Statistics
# Get total number of users
def grandUsers():
    query = "SELECT COUNT(*) FROM users"
    cur.execute(query)
    data = cur.fetchone()[0]
    return data


# Get total number of clients
def grandClients():
    query = "SELECT COUNT(*) FROM users WHERE role = 'c'"
    cur.execute(query)
    data = cur.fetchone()[0]
    return data


# Get total number of users
def grandDevs():
    query = "SELECT COUNT(*) FROM users WHERE role = 'd'"
    cur.execute(query)
    data = cur.fetchone()[0]
    return data


# Get best client with most project
def bestClient():
    query = "SELECT * FROM users WHERE finished_projects = (SELECT MAX(finished_projects) FROM USERS WHERE role = 'c') AND confirmed = 1 AND role = 'c'"
    cur.execute(query)
    data = cur.fetchall()
    return data


# Get best developer with most project
def bestDeveloper():
    query = "SELECT * FROM users WHERE finished_projects = (SELECT MAX(finished_projects) FROM USERS WHERE role = 'd') AND confirmed = 1 AND role = 'd'"
    cur.execute(query)
    data = cur.fetchall()
    return data


# Routes
# home page
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


# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    print("Login Page")
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
            rating = getUser(username)[5]
            session['warning'] = getUser(username)[6]
            session['description'] = getUser(username)[7]
            session['confirmed'] = getUser(username)[8]
            session['finished_projects'] = getUser(username)[9]
            session['interest'] = getUser(username)[10]
            session['sample_work'] = getUser(username)[11]
            session['business_credential'] = getUser(username)[12]
            session['balance'] = getUser(username)[13]
            session['logged_in'] = True
            if not session['finished_projects'] == 0:
                session['rating'] = rating / session['finished_projects']
            else:
                session['rating'] = 0.0
            if checkBlacklist(username):
                data = getBlacklist(username)
                session['logged_in'] = False
                return render_template("login.html", blacklist=data)
            if session['role'] != 'a':
                return redirect(url_for('dashboard'))
            else:
                return redirect(url_for('admin'))
        else:
            error = True
            return render_template("login.html", error=error)
    return render_template("login.html", error=error)


# register page
@app.route('/register', methods=['GET', 'POST'])
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


# dashboard page
@app.route('/dashboard')
def dashboard():
    isValidUser = False
    if session['logged_in']:
        isValidUser = True
        user_id = getUser(session['username'])[0]
        if session['role'] == 'd':
            role = 'Developer'
            active_bids = showActiveBidsDev(user_id)
            curr_projects = showActiveProjectsDev(user_id)
            history = showHistoryDev(user_id)
        elif session['role'] == 'c':
            role = 'Client'
            active_bids = showActiveBidsClient(user_id)
            curr_projects = showActiveProjectsClient(user_id)
            history = showHistoryClient(user_id)
        elif session['role'] == 'a':
            role = 'Admin'
            active_bids = ''
            curr_projects = ''
            history = ''
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

        if role == 'Client':
            return render_template("dashboard.html", confirmed=confirmed_user, isValidUser=isValidUser, role=role,
                                   client=True, active_bids=active_bids, curr_projects=curr_projects, history=history)
        if role == 'Developer':
            return render_template("dashboard.html", confirmed=confirmed_user, isValidUser=isValidUser, role=role,
                                   developer=True, active_bids=active_bids, curr_projects=curr_projects,
                                   history=history)
        if role == 'Admin':
            return render_template("dashboard.html", confirmed=confirmed_user, isValidUser=isValidUser, role=role,
                                   admin=True, active_bids=active_bids, curr_projects=curr_projects, history=history)
    else:
        return render_template("dashboard.html", isValidUser=False)


# navbar: Redirect link to profile page
@app.route('/profile')
def profile_redirect():
    print("Profile Redirect")
    return redirect(url_for('profile', username=session['username']))


# show profile
@app.route('/profile/<username>', methods=['GET'])
def profile(username):
    user_id = getUser(username)[0]
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
    if not finished_projects == 0:
        true_rating = rating / finished_projects
    else:
        true_rating = 0.0
    if confirmed != 0:
        confirmed_user = True
    elif confirmed == 0:
        confirmed_user = False

    if role == 'd':
        role = 'Developer'
        active_bids = showActiveBidsDev(user_id)
        curr_projects = showActiveProjectsDev(user_id)
        history = showHistoryDev(user_id)
    if role == 'c':
        role = 'Client'
        active_bids = showActiveBidsClient(user_id)
        curr_projects = showActiveProjectsClient(user_id)
        history = showHistoryClient(user_id)
    elif role == 'a':
        role = 'Admin'
        active_bids = ''
        curr_projects = ''
        history = ''

    return render_template("profile.html", email=email, role=role, first_name=first_name, last_name=last_name,
                           rating=true_rating, warning=warning, description=description, confirmed=confirmed_user,
                           finished_projects=finished_projects, interest=interest, sample_work=sample_work,
                           business_credential=business_credential, active_bids=active_bids,
                           curr_projects=curr_projects, history=history)


# compose page
@app.route('/compose', methods=['GET', 'POST'])
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
        balance = request.form['start_price']
        description = description.replace("'", "''")
        title = title.replace("'", "''")
        if postBid(title, description, start_price, deadline, file, visibility, user_id, balance):
            posting = showLatestPostByClient(session['user_id'])
            return render_template("post.html", post=posting)
        else:
            error = True
            return render_template("compose.html", error=error)
    else:
        return render_template("compose.html")


# admin page
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


@app.route('/admin/warn/<username>', methods=['GET', 'POST'])
def admin_warn(username):
    if session['logged_in'] == True:
        if session['role'] == 'a':
            adminWarnUser(username)
            link = '/profile/{}'.format(username)
            return redirect(link)
        else:
            return redirect(url_for('admin'))
    else:
        return redirect(url_for('admin'))


# admin: show all users
@app.route('/admin-users')
def admin_users():
    blacklist = adminBlacklist()
    all_users = adminUsers()
    return render_template("admin-users.html", blacklist=blacklist, users=all_users)


# admin: unban user
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


# admin: review project report
@app.route('/admin/take_action/<project_id>', methods=['GET', 'POST'])
def admin_takeaction(project_id):
    if request.method == 'POST':
        money = request.form['money']
        dev_rating = request.form['drating']
        client_rating = request.form['crating']
        old_dev_rating = findProject(project_id)[9]
        old_client_rating = findProject(project_id)[6]
        dev_id = findProject(project_id)[3]
        client_id = findProject(project_id)[4]
        price = findProject(project_id)[2]
        adminTakeAction(project_id, dev_rating, client_rating, old_dev_rating, old_client_rating, dev_id, client_id, money, price)
        session['balance'] = getUser(session['username'])[13]
        return redirect(url_for('admin'))
    else:
        return render_template('admin_takeaction.html', project_id=project_id)


# about page
@app.route('/about')
def about():
    number_of_users = grandUsers()
    number_of_clients = grandClients()
    number_of_devs = grandDevs()
    best_client = bestClient()
    best_dev = bestDeveloper()
    return render_template("about.html", all_users=number_of_users, all_clients=number_of_clients, all_devs=number_of_devs, best_client=best_client, best_dev=best_dev)


# show all posts in order of dates
@app.route('/posting', methods=['GET', 'POST'])
def postings():
    posts = showPosts()
    if request.method == 'POST':
        search_input = request.form['search']
        posts_result = postSearch(search_input)
        return render_template("postings.html", posts=posts_result)
    return render_template("postings.html", posts=posts)


# show specific post
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


# show all projects
@app.route('/project', methods=['GET', 'POST'])
def allProject():
    projects = allProjects()
    if request.method == 'POST':
        search_input = request.form['search']
        project_result = projectSearch(search_input)
        return render_template("project_all.html", posts=project_result)
    return render_template('project_all.html', posts=projects)


# show a specific project
@app.route('/project/<job_id>')
def project(job_id):
    post = showOnePost(job_id)
    # job_id, status, final_price, dev_id, client_id, dev_rating_desc, client_id, submit_text, submit_file, user_id, username, first_name, last_name
    project = findProjectAndDev(job_id)
    dates = findProjectDueDate(job_id)
    return render_template('project.html', post=post, project=project, date=dates)


# create a project and choose a developer if youre a client
@app.route('/project/<job_id>/<dev_name>/<price>/<project_days>', methods=['GET', 'POST'])
def projectCreate(job_id, dev_name, price, project_days):
    client_id = session['user_id']
    dev_id = getUser(dev_name)[0]
    if checkProjectBalance(client_id, price):
        createProject(job_id, dev_id, client_id, price, project_days)
        session['balance'] = getUser(session['username'])[13]
        return redirect(url_for('project', job_id=job_id))
    else:
        flash('You dont have enough balance')
        return redirect(url_for('post', job_id=job_id))


# developer: submit a project
@app.route('/project/<job_id>/submit/<dev_id>', methods=['GET', 'POST'])
def projectSubmit(job_id, dev_id):
    if request.method == 'POST':
        description = request.form['description']
        file = request.form['file']
        description = description.replace("'", "''")
        submitProject(job_id, dev_id, description, file)

        return redirect(url_for('project', job_id=job_id))
    else:
        return render_template('project_submit.html', job_id=job_id, user_id=dev_id)


# client: terminate a project
@app.route('/project/<job_id>/terminate/<client_id>', methods=['GET', 'POST'])
def projectTerminate(job_id, client_id):
    if request.method == 'POST':
        # terminate project and do some stuff on database
        return render_template('project_terminate.html', job_id=job_id)
    else:
        return render_template('project_terminate.html', job_id=job_id)


# Submit a review
@app.route('/project/<job_id>/review/<username>', methods=['GET', 'POST'])
def projectReview(job_id, username):
    if request.method == 'POST':
        description = request.form['description']
        rating = int(request.form['rating'])
        role = session['role']
        user_id = getUser(username)[0]
        if role == 'c':
            if rating < 3:
                status = 'Admin Review'
                # Client will give a review to developer
                giveProjectReviewForDeveloper(job_id, user_id, description, rating, status)
            else:
                status = 'Completed'
                developerTransferRemaining(job_id, user_id)
                giveProjectReviewForDeveloper(job_id, user_id, description, rating, status)
        else:
            # Developer give review to client
            giveProjectReviewForClient(job_id, user_id, description, rating)
        return redirect(url_for('project', job_id=job_id))
    else:
        return render_template('project_rating.html', job_id=job_id, username=username)


# edit profile
@app.route('/edit-profile', methods=['GET', 'POST'])
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


# Deposit money
@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    # if method post redirect to dashboard
    print('deposit')
    if request.method == 'POST':
        amount = request.form['balance']
        username = session['username']
        depositMoney(username, amount)
        return render_template("deposit.html", success=True)
    else:
        return render_template("deposit.html")


# withdraw money
@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    # if method post redirect to dashboard
    if request.method == 'POST':
        amount = request.form['balance']
        username = session['username']
        if withdrawMoney(username, amount):
            return render_template("withdraw.html", success='True')
        else:
            return render_template("withdraw.html", success='False')
    return render_template("withdraw.html")


# sign out
@app.route('/signout')
def signout():
    session['logged_in'] = False
    session.clear()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
