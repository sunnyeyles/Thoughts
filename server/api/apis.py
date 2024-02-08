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



def create_new_post(user_id, post_body, image):
    try:
        posts_connection = sqlite3.connect("posts.db")
        users_connection = sqlite3.connect("users.db")
        
        posts_cursor = posts_connection.cursor()
        users_cursor = users_connection.cursor()

        posts_cursor.execute("INSERT INTO posts (post_body, image) VALUES (?, ?)", (post_body, image))
        posts_connection.commit()

        posts_connection.close()
        users_connection.close()

        return True 
    except Exception as e:
        print(f"Error creating new post: {e}")
        return False  

def get_post_from_db(post_id):
    try:
        connection = sqlite3.connect("posts.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM posts WHERE post_id = ?", (post_id,))
        post = cursor.fetchone() 
        connection.close()
        return post
    except Exception as e:
        print("Error:", e)
        return None
