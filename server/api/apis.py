from flask import jsonify
import sqlite3


def get_all_records():
    connection = sqlite3.connect("gta.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM posts")
    records = cursor.fetchall()
    print(records)
    connection.close()
    return records


def get_user_by_id(year):
    connection = sqlite3.connect("gta.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM gta WHERE release_year = {year}")
    records = cursor.fetchall()
    connection.close()
    return records


def add_user(user):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users VALUES (?,?,?)", (user["email"], user["name"], user["city"])
    )
    connection.close()



def get_all_posts_from_db():
    try:
        
        connection = sqlite3.connect("./database/posts.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM posts")
        posts = cursor.fetchall()
        connection.close()
        return posts
    except Exception as e:
        print("Error:", e)
        return None
