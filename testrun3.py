import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()

sql = "insert into members values (?, ?, ?, ?, ?, ?)"
data = ((1, "Jesse", "Faas", 22, "faasjd@dukes.jmu.edu", "I was born and raised in Mechanicsville, Virginia. I went to Atlee high school where I began to study coding languages"))
cursor.execute(sql, data)
conn.commit()

sql2 = "insert into membersclone values (?, ?, ?, ?, ?, ?)"
data2 = ((2, "EsseJ", "Saaf", 44, "djsaaf@dukes.jmu.edu", "I am the clone"))
cursor.execute(sql2, data2)
conn.commit()
conn.close()
