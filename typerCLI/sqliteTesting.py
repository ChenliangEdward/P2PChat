import sqlite3

con = sqlite3.connect("main.db")
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE messages
               (timestamp text, from_user text, to_user text, content text)''')

# Insert a row of data
cur.execute("INSERT INTO messages VALUES ('2006-01-05','Edward','Wang','Hello World!')")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
