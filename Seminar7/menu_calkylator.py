
poisnenie = ('--------------------------\n'
    'Это программа калькулятор!\n'
'Основные правила:\n'
'Вводите арифметическое выражение со знаками без пробелов слитно в строчку\n'
'У вас два варианта выбора, кнопки на клавеатуре 2 и 3, выход из программы 4\n'
'---------------------------------------------------')
print(poisnenie)

def input_name():
    return input('Введите имя: ')


def menu_calkylator():
    x = input('Выберите варианты уравнения с:\n (2)рациональными числами; (3)комплексными числами (4) Выход из программы\nВвод: ')
    while True:
        try:
            x = int(x)
            if x <= 1 or x > 4: # тут можно ввести три числа 2 3 и 4 которое понадобится для цикла while и выхода
                x = input('Введите корректное число\n')   
            else:
                break
        except ValueError: 
            x = input("Вы ввели не число. Повторите ввод\n")
    return x
