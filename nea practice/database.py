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


def create_user(username,password):
    role = "Student"

    Hashed = werkzeug.security.generate_password_hash(password)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username,PasswordHash,Role) VALUES (?,?,?)",  (username, Hashed, role))
    conn.commit()
    conn.close()
