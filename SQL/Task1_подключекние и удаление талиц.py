import sqlite3 as sq

with sq.connect('E:\Programming\Visual_Studio_Code\Python_seminars_replay\SQL\saper2.db') as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS users") # удаляет таблицу
    cur.execute(""" CREATE TABLE IF NOT EXISTS users (
        
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER)
         """) # создать таблицу с именем users в скобках какая будет структура набор полей
                # IF NOT EXISTS - так ругаться уже не будет если добавить 

    # cur.execute("DROP TABLE users") # удаляет таблицу

# при создании каких либо полей можно делать ограничители
# если мы хотим чтобы name TEXt никогда не было пустым мы добавим  name TEXT NOT NULL
# или можем исподльзовать такой оггрничитель sex INTEGER DEFAULT 1 - это означает что по умолчанию, если 
# мы не будем передавать в поле sex  какое либо значение, то туда будет записано значение равное 1

# И еще добавляют sex INTEGER NOT NULL DEFAULT 1 - что то там езе записано, но по умолчанию принимается 1


# и в любой таблице еще  могут создаваться такие вот поля user_id INTEGER PRIMARY KEY - мы создаем поле
# user_id оно будет целочисленное INTEGER  и оно будет являться главным ключом PRIMARY KEY 
# это означает что user_id содержит уникальные значения

#  можно прописать ограничитель мы будем удалять только если существует зада данных 
# cur.execute("DROP TABLE IF EXIXTS users")

# еще прописывают к user_id INTEGER PRIMARY KEY AUTOINCREMENT чтобы значение user_id увеличивать на 1
   