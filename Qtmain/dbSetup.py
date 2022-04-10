import sqlite3
import os

os.remove("main.db")
con = sqlite3.connect("main.db")
cur = con.cursor()

# Create message Table
cur.execute('''CREATE TABLE messages
               (timestamp text, user text, inOrOut text, content text)''')
cur.execute('''CREATE TABLE friends
               (username text, ip text)''')

# Insert a row of messages
cur.execute("INSERT INTO messages VALUES ('1649558533','JoeB','In','I think I should resign.')")
cur.execute("INSERT INTO messages VALUES ('1649558563','JoeB','Out','Why not?')")
cur.execute("INSERT INTO messages VALUES ('1649558565','TimChen','Out','He wanna resign')")
cur.execute("INSERT INTO messages VALUES ('1649558575','TimChen','In','For real Man?')")

# Insert myself to db
cur.execute("INSERT INTO friends VALUES ('TimChen','10.0.0.2')")
cur.execute("INSERT INTO friends VALUES ('JoeB','10.0.0.3')")

con.commit()
con.close()
