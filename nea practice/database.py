import sqlite3

import werkzeug


# con = sqlite3.connect("Bookings.db")
# cursor = con.cursor()
#
# cursor.execute("INSERT INTO test (Field1) Values (9)")
#
#
# con.commit()
#
# con.close()

#this creates a new user when user signs up
def create_user(username,password):
    role = "Student"

    Hashed = werkzeug.security.generate_password_hash(password)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username,PasswordHash,Role) VALUES (?,?,?)",  (username, Hashed, role))
    conn.commit()
    conn.close()
#this fucntion should fetch the data based on a username
def fetch_users(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT UserID, Username, PasswordHash, Role FROM Users WHERE Username = ?", (username,))#the fact that the username parameter at the end didnt have a comma meant this code was broken for a long ammount of time:(
    row = cursor.fetchone()
    conn.close()
    return row