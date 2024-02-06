from flask import jsonify
import sqlite3


def get_all_records():
    connection = sqlite3.connect("gta.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM gta")
    records = cursor.fetchall()
    connection.close()
    return records
    
def get_user_by_id(year):
    connection = sqlite3.connect("gta.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM gta WHERE release_year = {year}")
    records = cursor.fetchall()
    connection.close()
    return records

def get_all_posts():
    records = get_all_records()
    return jsonify({'All posts': records})
    
    
def add_user(user):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users VALUES (?,?,?)", (user['email'], user['name'], user['city']))
    connection.close()


def add_post_to_database(post):
    connection = sqlite3.connect("posts.db")
    cursor = connection.cursor()
    # fix this
    cursor.execute("INSERT INTO posts (?,?,?)", (user['email'], user['name'], user['city']))

    print("Yo")
