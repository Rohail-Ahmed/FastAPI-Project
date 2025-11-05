import sqlite3
from fastapi import FastAPI,HTTPException

def connect_db():
    return sqlite3.connect('users.db')

# create table
conn = connect_db()
conn.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT                           
            )
""")
conn.commit()
conn.close()

def add_user(username,password):
    conn = connect_db()
    cursor = conn.execute("INSERT INTO users (username,password) VALUES (?,?)",(username,password))
    conn.commit()
    conn.close()

def get_user(username,password):
    conn = connect_db()
    cursor = conn.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
    user = cursor.fetchone()
    conn.close()
    return user

def get_all_users():
   conn = connect_db()
   cursor = conn.execute("SELECT id, username FROM users")
   data =cursor.fetchall()
   conn.close()
   return data

def update_user(user_id,new_username):
    conn = connect_db()
    conn.execute("UPDATE users SET username=? WHERE id=?",(new_username,user_id))
    conn.commit()
    conn.close()

def delete_user(user_id,):
    conn = connect_db()
    conn.execute("DELETE FROM users WHERE id=?",(user_id,))
    conn.commit()
    conn.close()