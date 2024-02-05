import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE users (email TEXT, name TEXT, city TEXT)")

user_data = [
    ("john@example.com", "John Doe", "New York"),
    ("alice@example.com", "Alice Smith", "San Francisco"),
    ("bob@example.com", "Bob Johnson", "Los Angeles"),
    ("emma@example.com", "Emma Davis", "Chicago"),
    ("david@example.com", "David Brown", "Miami")
]

# Insert data into the table
cursor.executemany("INSERT INTO users VALUES (?, ?, ?)", user_data)

# Commit the changes
connection.commit()

# Close the connection
connection.close()