import model_kalk 

poisnenie = ('Это программа калькулятор!\n'
'Основные правила:\n'
'Вводите арифметическое выражение со знаками без пробелов слитно в строчку\n'
'У вас три варинта выбора, кнопки на нлавеатуре 2, 3, 4\n')

def calkylator():
    while True:
        try:
            x = int(input('Выберите варианты уравнения с:\n (2)рациональными;   (3)комплексными)\nВвод: '))
            while x <= 1 or x > 4:
                x = int(input('Введите корректное число')   ) 
        except ValueError: print("Вы ввели не число. Повторите ввод")
        else:
            if x == 2: 
                print('рациональные')
                return model_kalk.my_eval(expresion)
            elif x == 4: 
                print('комплексные')
                expresion = ''
                for element in input():
                    expresion += str(element)
                return model_kalk.my_eval(expresion)