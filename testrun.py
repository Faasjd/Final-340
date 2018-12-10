import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
sql = "create table celebs (celebID integer PRIMARY KEY, firstname text, lastname text, age integer, email text, photo text, bio text)"
cursor.execute(sql)
conn.commit()

sql2 = "create table members (memberID integer PRIMARY KEY, firstname text, lastname text, age integer, email text, bio text)"
cursor.execute(sql2)
conn.commit()

sql3 = "create table membersclone (memberID integer PRIMARY KEY, firstname text, lastname text, age integer, email text, bio text)"
cursor.execute(sql3)
conn.commit()


conn.close()
