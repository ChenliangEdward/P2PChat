import sqlite3
import datetime

con = sqlite3.connect("main.db")
cur = con.cursor()
# for row in cur.execute('''SELECT * FROM messages WHERE user='TimChen' ORDER BY timestamp'''):
#     print(row)
#     print(type(row))

name = "JoeB"
allMsg = ""
sender = ""
at = ""

# get all msg related to the selected person
for row in cur.execute(f'''SELECT * FROM messages WHERE user='{name}' ORDER BY timestamp '''):
    sender = "Me" if row[2] == "Out" else row[1]
    at = str(datetime.datetime.fromtimestamp(int(row[0])))
    content = row[3]
    curMsg = f"\n{at}\n{sender}:\n{content}\n"
    allMsg = allMsg + curMsg
print(allMsg)
