
import programs as pr
import menu as menu
import del_syroki as del_s
import proverka_del as prov
import izmenit as imp
import import_bd as imports
import eksport_bd as exs

def button_click():
    print('\nИнформационная система позволяющая работать с сотрудниками некой компании\n'
          '---------------------------------------------------------------------------')
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
            imp.izm()
        elif x == 4: 
            print('Импорт нашей БД, показываем на экране')
            imports.imports()
        elif x == 5: 
            print('Экспорт БД')
            exs.eksport()
    else: 
        print ('выход из программы') 
      