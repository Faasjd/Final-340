import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
data = '''update celebs set photo=replace(photo,'nphinity','software4rfid')'''
cursor.execute(data)
conn.commit()
conn.close()
