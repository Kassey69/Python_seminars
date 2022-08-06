
from programma import *

with db:
    db.create_tables([name_nama, department, post])
    kommunalka = name_nama(name=('Введите')).save()
    benzin = name_nama.create(name ='1212')
    ineet = name_nama.insert(name ='1212').execute()
    

print('DONE')
