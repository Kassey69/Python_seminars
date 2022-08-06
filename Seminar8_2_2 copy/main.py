
from programma import *

with db:
    mod = str(input('Введи имя'))
    # mod2 = str(input('Введи имя'))
    # db.create_tables([namer, department,  post])
    Name = namer(name = mod).save() # лучший метод 
    # Telefon = namer(phone = mod2).save()
    # Telefon = name_nama.create(name = input('Введи телефон')) # средний 
    # ine3et = name_nama.insert(name =('sdf')).execute() # хучший метод 
    deh = department(name = input('Введи имя')).save()
    

print('DONE')
