# связующее звено между двумя модулями model и view

import modul_complex as complex
import modul_rasional as rasional
import view
import menu_calkylator as m_сalk
import logger
# import polzovatel as p

def button_click():
    name = m_сalk.input_name()
    x = m_сalk.menu_calkylator()
    while x != 4:
        if x == 2:
            #  print('Ввод ')
             a = view.get_value()
             result = rasional.my_eval(a)
            #  p.polz(a, result)
             s = f'Имя пользователя: {name}  выражение: {a};  результат: {result}'
             logger.log_data(s)
        elif x == 3:
            #  print('Ввод ') 
             a = view.get_value()
             result = complex.my_eval(a)
        x = m_сalk.menu_calkylator()
    else: 
        print('выход из программы')


   
   

  
