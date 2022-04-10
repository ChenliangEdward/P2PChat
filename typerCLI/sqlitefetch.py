import sqlite3

con = sqlite3.connect("main.db")
cur = con.cursor()

for row in cur.execute('SELECT * FROM messages ORDER BY timestamp'):
    print(row)
    print(type(row))
