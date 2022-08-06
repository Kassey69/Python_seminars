#*Задание в группах:** Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах. 
# под форматами понимаем структуру файлов, например:в файле на одной строке хранится одна часть записи, 
# пустая строка - разделитель*
#     *Фамилия_1*
#     *Имя_1*
#     *Телефон_1* 
#     *Описание_1*
#     *Фамилия_2*


# еще вариант как распечатать все и сразу
from base64 import encode
import encodings
import json


name = input('Введиет имя')
tel = input('Ввкедите телефон')
comment = input( 'Введите коментарии')  
with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_1\sle_file.txt', 'a+', encoding='utf-8') as file:
     file.write(', '.join([name, tel, comment]) + '\n')

# Провильное заполнение джейсона

json_tel = {tel: {
                'name': name,
                'comment': comment
                }
}

json_tel[tel] = {'name': name, 'comment':comment}
for a,b in json_tel.items():
    print(a,b)



import json

def names(): 
    global name, number, comment
    name = input('Введиет имя')
    number = input('Ввкедите телефон')
    comment = input( 'Введите коментарии')
    # ключ это i в нем хранится 3 значения
    return name, number, comment


def slovar():
    names()
    data = (number, comment)
    book = {}
    book[name] = data
    # return str(book.items())
    return book

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


redus = slovar()
# джейсон
# Метод позволяет записать текст в файл
def save_file_json():
    with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_1\slovar_file.json', 'a', \
        encoding='utf-8') as file:
        file.write(json.dumps(redus, ensure_ascii=False)+',\n')
        file.close()
        print('')

def load_file_json():
    with open('E:\Programming\Visual_Studio_Code\Python_seminars_replay\Seminar8_1\slovar_file.json', 'r', \
        encoding='utf-8') as file:
         result = json.load(file)
         
         return result

# ee = slovar(r) 
# print(ee)       
# save_file()
# load_file()

save_file_json()
# f = load_file_json()
# print((f))





# d2 = {"id": 1948, "name": "Washer", "size": 3}

# with open('out.txt','w') as out:
#     for key,val in d2.items():
#         out.write('{}:{}\n'.format(key,val))



# print(sborka(newlist))
# temp = sborka(newlist) 

# file_end = temp # создаем файл и передаем значения нашего полинома
# with open('polynomial_end.txt', 'w') as data:
#     data.write(file_end)






