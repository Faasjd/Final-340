import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
sql = "select *from members"
cursor.execute(sql)

rows = cursor.fetchall()

for row in rows:
    print (row)

cursor = conn.cursor()
sql = "select *from celebs"
cursor.execute(sql)

rows = cursor.fetchall()

for row in rows:
    print (row)


cursor = conn.cursor()
sql = "select *from membersclone"
cursor.execute(sql)

rows = cursor.fetchall()

for row in rows:
    print (row)
conn.close()
