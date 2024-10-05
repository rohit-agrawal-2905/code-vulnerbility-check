# app.py - Sample Python application with a security flaw (SQL Injection)

import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    # Unsafe user input that can lead to SQL Injection vulnerability
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    result = cursor.fetchall()
    conn.close()
    return f'User: {result}'

if __name__ == '__main__':
    app.run(debug=True)
