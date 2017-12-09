# This file will not be used anymore (probably)



# # this file inserts mock data to the database
# import pymysql


# conn = pymysql.connect(host='localhost', port=3306, user='root', password='password', db='cd-marketplace', autocommit=True)
# cur = conn.cursor()

# # Insert mock data to users table
# # NOTE: developer and client are single chars
# cur.execute("INSERT INTO users (email, password, username, role) VALUES ('chrispanican@gmail.com', 'webapp1', 'chris1800', 'd')")
# cur.execute("INSERT INTO users (email, password, username, role) VALUES ('helloworld@gmail.com', 'webapp2', 'helloworld123', 'c')")
# cur.execute("INSERT INTO users (email, password, username, role) VALUES ('Harold_Pain@yahoo.com', 'webapp3', 'harold_pain', 'd')")

# # NOTE: When a user is created, a profile is created as well
# # Insert mock data to profile table
# cur.execute("INSERT INTO profile (first_name, last_name, description) VALUES ('Chris', 'Panican', 'Im an aspiring developer.')")
# cur.execute("INSERT INTO profile (first_name, last_name, description) VALUES ('Hello', 'World', 'I have many project requests.')")
# cur.execute("INSERT INTO profile (first_name, last_name, description) VALUES ('Harold', 'Pain', 'I like to earn money.')")

# # Post
# # client_id is the one who requested the post
# cur.execute("INSERT INTO post (title, description, price, deadline, bidding_time, client_id) VALUES ('Please help me with my database', 'My database is messed up and I need help PLEASE!! The instructions are..','50', '2017-12-31 00:00:00', '3', '2')")

# # Project
# # Generated after bid ends. Deadline and description carries over from post
# cur.execute("INSERT INTO project (status, final_price, dev_id, client_id) VALUES ('Ongoing', '50', '1', '2')")

# # New_users
# # User_id is inserted manually
# cur.execute("INSERT INTO new_users (username, role, email, password) VALUES ('ayylmao', 'd', 'ayylmao@gmail.com', '1234')")

# # Blacklist
# # User_id is inserted manually
# cur.execute("INSERT INTO blacklist (user_id, reason) VALUES ('3', 'He posted a banned meme on site.')")

# query = 'SELECT * FROM users'
# cur.execute(query)
# data = cur.fetchall()
# print(data)