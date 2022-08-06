def menu_proverka():
    x = input('Введите номер числа отвечающий за должность, сотрудник будет удален\nВвод: ')
    while True:
            try:
                x = int(x)
                if x < 1 or x > 6: # тут можно ввести три числа 2 3 и 4 которое понадобится для цикла while и выхода
                    x = input('Введите корректное число\n')  
                else:
                    break
            except ValueError: 
                x = input("Вы ввели не число. Повторите ввод\n") 
    return x