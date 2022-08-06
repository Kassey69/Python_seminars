import programs as pr
import menu as menu
import del_syroki as del_s
import proverka_del as prov


def button_click():
    x = menu.menu()
    while x != 6:
        if x == 1: 
            print('добавить сотрудника')
            pr.wef() 
        elif x == 2: 
            print('удалить сотрудника')
            del_s.delet()
        elif x == 3: 
            print('Изменить данные')
            return 
        elif x == 4: 
            print('Импорт БД')
            return 
        elif x == 5: 
            print('Экспорт БД')
            return 
    else: 
        print ('выход из программы') 
