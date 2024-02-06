import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE users (email TEXT, name TEXT, city TEXT, user_id TEXT PRIMARY KEY)")

user_data = [
    ("john@example.com", "John Doe", "New York", "sddfgsdfgsfgerergdf"),
    ("alice@example.com", "Alice Smith", "San Francisco", "dssadfreferf"),
    ("bob@example.com", "Bob Johnson", "Los Angeles", "sfasfrefrer"),
    ("emma@example.com", "Emma Davis", "Chicago", "eesdccer344f"),
    ("david@example.com", "David Brown", "Miami", "dsferfdsfer")
]

# Insert data into the table
cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", user_data)

# Commit the changes
connection.commit()

# Close the connection
connection.close()