
def names(): 
    global name, number, comment
    name = input('Введиет имя')
    number = input('Ввкедите телефон')
    comment = input( ' Введите коментарии')
    # ключ это i в нем хранится 3 значения
    return name, number, comment











# def Intface(i:str):
#     match i:
#         case "Ir":
#             return [input(' Введите данные')]
#         case "Camp":
#             x = input ( ' Введите фамилию')
#             y = input ( ' Введите Имя')
#             z = input ( ' Введите телефон')
#             h = input ( ' Введите описание')

#             match i:
#                 case 'str': return x+y+ z+h
            
# print(Intface())