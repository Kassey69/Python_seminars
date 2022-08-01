# связующее звено между двумя модулями model и view

import modul_complex as c
import modul_rasional as rasional
import view
import menu_calkylator as m_сalk
import logger
import polzovatel as p

def button_click():
    name = m_сalk.input_name()
    x = m_сalk.menu_calkylator()
    while x != 4:
        if x == 2:
           kol = 2
           for i in range(2):
             kol -= i 

             print('Ведите числа')
             a = view.get_value()
             result = rasional.my_eval(a)
             p.polz(a, result)
             s = f'Имя пользователя: {name}  выражение: {a};  результат: {result}'
             logger.log_data(s)

             print( f'До возврата в главное меню осталось {kol} ходов')
           m_сalk.menu_calkylator()
        elif x == 3:
           kol = 2
           for i in range(2):
             kol -= i 

             print('Ведите числа') 
             a = view.get_value()
             result = c.parentheses(c.list_of_numbers_and_operations(a))
         
             p.polz(a, result)
             s = f'Имя пользователя: {name}  выражение: {a};  результат: {result}'
             logger.log_data(s)

             print( f'До возврата в главное меню осталось {kol} ходов')
           m_сalk.menu_calkylator()
    else: 
        print('выход из программы')


   
   

  
