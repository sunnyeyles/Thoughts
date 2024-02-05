from flask import jsonify
import sqlite3

def get_all_records():
    connection = sqlite3.connect("gta.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM gta")
    records = cursor.fetchall()
    connection.close()
    return records
    
def get_all_records():
    connection = sqlite3.connect("gta.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM gta")
    records = cursor.fetchall()
    connection.close()
    return records
    
def get_record_by_year(year):
    connection = sqlite3.connect("gta.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM gta WHERE release_year = {year}")
    records = cursor.fetchall()
    connection.close()
    return records

def get_all_gta_records():
    records = get_all_records()
    return jsonify({'gta_records': records})
    
    
def add_user(user):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO users VALUES (?,?,?)", (user['email'], user['name'], user['city']))
    connection.close()
