import sqlite3


connect = sqlite3.connect("users.db")

cursor = connect.cursor()
  
cursor.execute("""CREATE TABLE IF NOT EXISTS users( 
   user_id INTEGER, 
   user_name TEXT,
   age INTEGER,
   telefon INTEGER
)
""")
connect.commit()
connect.close()