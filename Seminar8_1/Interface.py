

def Intface(i:str):
    match i:
        case "Welcome":
            print('---------------------------------------------')
            print('Здравствуйте')
        case "Menu":
            print('---------------------------------------------')
            print('МЕНЮ СПРАВОЧНИКА')
            print('1. Импортиовать данные в справочник')
            print('2. Экспортировать данные из справочника')
            print('3. добавление данных в справочник')
            print('4. Выход из справочника')
        case "End":
            print('----------------------------------------------')
            print('Выберите дальнейшее действие')
            print('1. Выход в главное меню')
            print('2. Выход из программы')
