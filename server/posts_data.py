import sqlite3

connection = sqlite3.connect("posts.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE posts (post-body TEXT, FOREIGN KEY(id) REFERENCES users(user_id))")

post_data = [
    ("something somethiung bla ewfa bla", "oifqidwfqiehoipwej"),
    ("something somethiung bla bladsccsdcd bla", "oiherifdwfqiehoipwej"),
    ("something somethiung blwefa bla", "oiherifqidwfhoipwej"),
    ("something somethiung bla blasddsca bla", "oiherifqidwfqieej"),
]

# Insert data into the table
cursor.executemany("INSERT INTO posts VALUES (?, ?)", post_data)

# Commit the changes
connection.commit()

# Close the connection
connection.close()
