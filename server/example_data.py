import sqlite3

connection = sqlite3.connect("gta.db")
cursor = connection.cursor()

# Drop the table if it already exists
cursor.execute("DROP TABLE IF EXISTS gta")

# Create the table
cursor.execute("CREATE TABLE gta (release_year INTEGER, release_name TEXT, city TEXT)")


# Add a new column with a default value

release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2013, "Grand Theft Auto V", "Los Santos")
]

# Insert data into the table
cursor.executemany("INSERT INTO gta VALUES (?, ?, ?)", release_list)

# Commit the changes
connection.commit()

# Close the connection
connection.close()
