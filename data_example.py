import sqlite3

def get_total():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT * FROM stocks')
    total = 0
    for item in c.fetchall():
        total += item[2] * item[3]
    return total