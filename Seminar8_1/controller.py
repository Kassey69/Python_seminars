import views
import progravva as pr
import meny
import schit_zapis as sz

def button_click():
    name = views.names()
    slovar = pr.slovar(name)
    x = meny.menu_spravochnik()
    while x != 4:
        if x == 1:
             print('Импортиовать данные в справочник')
             s = f'Имя пользователя: {slovar}  '
             sz.write_file(s)

          
        elif x == 2:
            print('Импортиовать данные в справочник')
            s = f'Имя пользователя: {slovar}  '
            sz.write_file(s)

        
   
    
    else: 
        print('выход из программы')