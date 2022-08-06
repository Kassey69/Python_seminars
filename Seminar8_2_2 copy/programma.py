import sqlite3
import datetime
from peewee import *

# документация по пиви # https://docs.peewee-orm.com/en/latest/index.html

db = SqliteDatabase('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2_2 copy\gitudata.db')


# еще нуно создать базывый класс всех класов
# он включает в себя общие инствукции, а вссе остальные модели наследуются от него

class BaseModel(Model):
    id = PrimaryKeyField(unique=True) # уникальный перввичный ключ, данные из этого поля будут
 # уникалными идентификаторами записи
    class Meta:
        database = db 
        order_by = 'id' 

# поля объектов , они же являются столбцами таблиц в базе данных
class namer(BaseModel):
    # id = PrimaryKeyField(unique=True)
    name = CharField()  # тут мы будем хранить текст, поэтому указываем его тип как симвотльное поле
    # phone = TextField()
# TextField()
#CharField()
    class Meta:
        db_table = 'namer'  # та таблица которая нужна нам    

class department(BaseModel):
    # id = PrimaryKeyField(unique=True)   
    department_name = CharField()
    name_id = ForeignKeyField(namer) # ссылка на всю запись - id = PrimaryKeyField(unique=True)в верхней модели

    class Meta:
        db_table = 'department'    

class post(BaseModel):
    # id = PrimaryKeyField(unique=True)   
    post_name = CharField()
    department_id = ForeignKeyField(namer) # ссылка на всю запись

    class Meta:
        db_table = 'post' 




































# # поля объектов , они же являются столбцами таблиц в базе данных
# class name(Model):
#     id = PrimaryKeyField(unique=True)
#     name = CharField()  # тут мы будем хранить текст, поэтому указываем его тип как симвотльное поле
#     telefon = CharField()


#     class Meta:
#         database = db 
#         db_table = 'name' # та таблица которая нужна нам
      

# class department(Model):
#     id = PrimaryKeyField(unique=True)   
#     department_name = CharField()
#     name_id = ForeignKeyField(name) # ссылка на всю запись - id = PrimaryKeyField(unique=True)в верхней модели

#     class Meta:
#         database = db 
#         db_table = 'department'    

# class post(Model):
#     id = PrimaryKeyField(unique=True)   
#     post_name = CharField()
#     department_id = ForeignKeyField(department) # ссылка на всю запись

#     class Meta:
#         database = db 
#         db_table = 'post' 

























    # метакласс это класс внутри класса
    # class Meta:
    #     database = db # c какой базой работает модель
    #     order_by = 'id_name' # какие поля будут сортироваться по умолчанию
    #     ви_ефиду = 'name' # указываем мена таблиц которые нужны нам
    # # таблицы нужно называть именем сушнсти во множественном числе а поля в единственном































# # Создание базы


# with sqlite3.connect('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\database.db') as db:
#     cursor = db.cursor()
#     query = """ CREATE TABLE IF NOT EXISTS expenses (id INTEGER, name TEXT) """
#     cursor.execute(query)


# # СОЗДАЕМ ТАБЛИЦУ ЕСЛИ ТАКОЙ ЕЩЕ НЕТ С ИМЕНЕМ expenses И двумя полями id и name с итпами данных INTEGER и TEXT
# # ПРОИЗВОДИМ NT ЖЕ САМЫ ЕДЙСТВИЯ НО УЖЕ МЕНЯЕМ СЧТРОКУ ЗАПРОСОВ
#     query1 = """ INSERT INTO expenses(id, name) VALUES(1, 'КОММУНАЛКА' )  """
#     query2 = """ INSERT INTO expenses(id, name) VALUES(2, 'БЕНЗИН' )  """
#     query3 = """ INSERT INTO expenses(id, name) VALUES(3, 'ИНТЕРНЕТ' )  """
#     # cursor.execute(query1)
#     # cursor.execute(query2)
#     # cursor.execute(query3)
#     db.commit()

# def get_timestamp(y,m,d):
#     return datetime.datetime.timestamp(datetime.datetime(y,m,d))

# def get_date(tmstmp):
#     return datetime.datetime.fromtimestamp(tmstmp).date()


# # # ЧТОБЫ все сделать в одну строчку делаем
# insert_payments = [
#     (1, 120, get_timestamp(2020, 9, 1), 1), # создаем картэжи и добавляем в них данные а затем передаем в виде
#     (2, 12, get_timestamp(2020, 9, 1), 1),  # аргумента методу imsert_payment, а первым аргументом
#     (3, 10, get_timestamp(2020, 9, 1), 1), #  а первым аргументом  будет запрос к базе данных на добавление строк
#     (4, 120, get_timestamp(2020, 9, 1), 1),
#     (5, 120, get_timestamp(2020, 9, 1), 1),
#     (6, 120, get_timestamp(2020, 9, 1), 1),
#     (7, 120, get_timestamp(2020, 9, 1), 1)
#  ]
# # # а первым аргументом  будет запрос к базе данных на добавление строк? 
# # # мы укахз-ываем порядок полей и соответствующие порядок значения этих полей


# with sqlite3.connect('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\database.db') as db:
#     cursor = db.cursor()
#     query = """ CREATE TABLE IF NOT EXISTS payments(
#         id INTEGER,
#         amount REAL,
#         payment_date INTEGER,
#         expense_id INTEGER)"""
#     cursor.execute(query)
#     db.commit()   
#     query =""" INSERT INTO payments(id, amount, payment_date, expense_id)
#                                                     VALUES(?,?,?,?); """
#     cursor.executemany(query, insert_payments)
#     db.commit()
#     print(cursor.rowcount, "строк добавлено")


# #_____________________________
# # Получение информации из базы
# #_____________________________

# with sqlite3.connect('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\database.db') as db:
#     cursor = db.cursor()
#     query = """ SELECT * FROM payments"""
#     cursor.execute(query)
#     sum = 0
#     for res in cursor:
#         sum += res[1]
#         print(res)
#     print('TOTAL:', sum)


# # выберем расходы только на бензин и получим общую сумму затрат только на бензин
# with sqlite3.connect('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\database.db') as db:
#     cursor = db.cursor()
#     query = """ SELECT amount, payment_date, name FROM payments JOIN expenses 
#                 ON expenses.id = payments.expense_id WHERE expense_id = 2"""

#     cursor.execute(query)
#     sum = 0
#     for res in cursor:
#         sum += res[0]
#         print(res[0], get_date(res[1]))
#     print('TOTAL:', sum)










































# получение информации из базы
 
# with sqlite3.connect('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_2\database.db') as db:
#     cursor = db.cursor()
#     query = """ CREATE TABLE IF NOT EXISTS payments(
#         id INTEGER,
#         amount REAL,
#         payment_date INTEGER,
#         expense_id INTEGER
#     )"""
#     cursor.execute(query)
#     db.commit()

 




# db = sqlite3.connect('server.db')
 
# sql = db.cursor()
# sql.execute("""CREATE TABLE IF NOT EXISTS list_of_courses_for_registration (course_name TEXT, author TEXT)""")
# db.commit()
 
# def reg():
#     course_name = input('Name: Погремушка Мамонтёнок ')
#     # course_name = course_name.decode('cp866').encode('utf-8')
#     author_course = input('Author: yar.yarn ')
#     sql.execute(f"SELECT course_name FROM list_of_courses_for_registration WHERE course_name = '{course_name}'")
#     if sql.fetchone() is None:
#         sql.execute(f"INSERT INTO list_of_courses_for_registration VALUES (?, ?)", (course_name, author_course))
#         db.commit()
#         print('Зарегистрировано!')
#     else:
#         print('Такая запись уже имеется!')
 
#     for value in sql.execute("SELECT * FROM list_of_courses_for_registration"):
#         print(f"Cource {value[0]}, Author {value[1]}")
 
# reg()

























# def user_data(): 
#     global name, number, comment
#     book = {}
#     name = input('Введите имя ')
#     number = input('Введите телефон ')
#     comment = input( 'Введите коментарии ')
#     # ключ это i в нем хранится 3 значени
#     data = (number, comment)
#     book[name] = data
#     # return str(book.items())
#     print(book)
#     return book


# # def pridaji():
  

# # def prinzvodstvo():


# # Метод позволяет записать текст в файл
# def save_file():
#     with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_1\slovar_file.txt', 'a', \
#         encoding='utf-8') as file:
#         file.writelines(f' {ee}\n')

# def load_file():
#     with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_1\slovar_file.txt', 'r', \
#         encoding='utf-8') as file:
#          r = file.read()
#          print(r)   


# # redus = slovar()
# # # джейсон
# # # Метод позволяет записать текст в файл
# # def save_file_json():
# #     with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_1\slovar_file.json', 'a', \
# #         encoding='utf-8') as file:
# #         file.write(json.dumps(redus, ensure_ascii=False)+',\n')
# #         file.close()
# #         print('')

# # def load_file_json():
# #     with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_1\slovar_file.json', 'r', \
# #         encoding='utf-8') as file:
# #          result = json.load(file)
         
# #          return result

# # ee = slovar(r) 
# # print(ee)       
# # save_file()
# # load_file()

# # save_file_json()
# # f = load_file_json()
# # print((f))


# def menu():
#     x = input(' Выберите соответствующий раздел:\n (1)Добавить сотрудника\n (2)Удалить сотрудника\n\
#  (3)Изменить данные сотрудника\n (4)Импорт базы данных\n (5)Экспорт базы данных\n (6)Выход из меню\nВвод ')
#     while True:
#         try:
#             x = int(x)
#             while x < 1 or x > 6:
#                 x = input('Введите корректное число\n ')      
#         except ValueError: 
#             x = input('Вы ввели не число. Повторите ввод\n ')
#         else: 
#             while x !=6:
#                 if x == 1: return user_data()
#                 elif x ==2: return 
#                 elif x ==3: return
#                 elif x ==4: return
#                 elif x ==5: return 
#             else: 
#                 print(' выход из программы ')
#                 break
# menu()


# def bugalteria():

#     x = input('Выберите должность:\n (1)главный бугалтер\n (2)помощник бугалтера\n (3)старший помощник бугалтера\n\
#  (4) Главное меню \nВвод  ' )
#     while True:
#         try:
#             x = int(x)
#             while x < 1 or x > 4:
#                 x = input('Введите корректное число\n')      
#         except ValueError: 
#             x = input('Вы ввели не число. Повторите ввод\n')
#         else: 
#             while x !=4:
#                 if x == 1: 
                    
#                     print(f' главный бугалтер зафиксировано!!!!')
#                     break

#                 elif x == 2: 
                  
#                     print(f' помощник бугалтера зафиксировано!!!')
                    
#                 elif x == 3: 
                  
#                     print(f' старший помощник бугалтера зафиксировано!!')
                  
#             else: 
#                 print(' выход в главное меню')
#                 break
#             return menu()





# def id_rabotniki_otdela():
#     x = input(' Выберите отдел:\n (1)бугалтерия\n (2)Продажи\n (3) Производствоn\n (4) Главное меню\nВвод ' )
#     while True:
#         try:
#             x = int(x)
#             while x < 1 or x > 4:
#                 x = input('Введите корректное число\n')      
#         except ValueError: 
#             x = input('Вы ввели не число. Повторите ввод\n')
#         else: 
#             while x !=4:
#                 if x == 1: 
                    
#                     print(f' Отдел бугалтерия защиксирован!!!\n')
#                     return bugalteria()

#                 # if x == 2: 
#                 #     a = user_data()
#                 #     print(f' Отдел продажи {a}')
#                 #     return prоdaji()
#                 # if x == 3: 
#                 #     a = user_data()
#                 #     print(f' Отдел продажи {a}')
#                 #     return prinzvodstvo()
#             else: 
#                 print(' выход в главное меню')
#                 return menu()
# id_rabotniki_otdela()






















