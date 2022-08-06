import sqlite3 as sq

with sq.connect('E:\Programming\Visual_Studio_Code\Python_seminars_replay\SQL\saper1.db') as con:
    cur = con.cursor()

   
    cur.execute(""" CREATE TABLE IF NOT EXISTS users (
        
     
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER)
         """) # создать таблицу с именем users в скобках какая будет структура набор полей
                # IF NOT EXISTS - так ругаться уже не будет если добавить 

    # cur.execute("DROP TABLE users") # удаляет таблицу

# Прописываем в программа  - INSERT INTO users VALUES ('мИХ', 1,19,1000) переходим на вкладку запись 
# и видим добавилась запись

    # 1 вариант 
    insert_payments = [
    ('мИХ', 1, 19, 1000)
    ]

    con = (""" INSERT INTO users (name, sex, old, score)
                                                    VALUES(?,?,?,?);""")
    cur.executemany(con, insert_payments)
    print(cur.rowcount, "строк добавлено") # на выходе полуучилось 'мИХ', 1, 19,  1000 
                                         

  # 2 вариант
    insert_payments = [
    ('sИХ', 32,  1000)
     ] 

    con = (""" INSERT INTO users (name,  old, score)
                                                    VALUES(?,?,?);""")
    cur.executemany(con, insert_payments)
    print(cur.rowcount, "строк добавлено") # на выходе полуучилось 'sИХ', 1, 32,  1000 
                                                    # добавилась 1 в поле sex

  # 3 вариант SELECT

    insert_payments = [
    ('Феcот', 32,  1000)
    ('Федот', 12,  100)
     ] 

    con = (""" SELECT * FROM users WHERE score < 1000
                                                   VALUES(?,?,?);""")
    cur.executemany( insert_payments,con)
    print(cur.rowcount, "строк добавлено") 

#   query3 = """ INSERT INTO expenses(id, name) VALUES(3, 'ИНТЕРНЕТ' )  """
# #     # cursor.execute(query1)