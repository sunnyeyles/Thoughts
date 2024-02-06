
import sqlite3

# Create the users table
connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE users (user_id TEXT PRIMARY KEY, email TEXT, username TEXT, password TEXT)")

user_data = [
    ("sddfgsdfgsfgerergdf", "john@example.com", "JohnDoe", "Nevewvwek"),
    ("dssadfreferf", "alice@example.com", "AliceSmith", "Sawerwrecsco"),

]

# Insert data into the users table
cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", user_data)

# Commit the changes
connection.commit()

# Close the connection
connection.close()

# Create the posts table
connection = sqlite3.connect("posts.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE posts (post_id TEXT PRIMARY KEY, post_body TEXT, user_id TEXT, FOREIGN KEY(user_id) REFERENCES users(user_id))")

post_data = [
    ("dsferfsdfvdsfesfsdr","something somethiung bla ewfa bla", "dsferfdsfer"),
    ("dsfedfvrfdsfesdfr","something somethiung bla bladsccsdcd bla", "dsferfdsfer"),

]

# Insert data into the posts table
cursor.executemany("INSERT INTO posts VALUES (?, ?, ?)", post_data)

# Commit the changes
connection.commit()

# Close the connection
connection.close()
