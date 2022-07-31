# 41. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный. 
    
#     *Пример:*    
#     2+2 => 4;     
#     1+2*3 => 7;     
#     1-2*3 => -5;
    
#     - Добавьте возможность использования скобок, меняющих приоритет операций.
        
#         *Пример:*         
#         1+2*3 => 7;         
#         (1+2)*3 => 9;

# def reshenie1():
        # n1 = random.randint(0,20)
        # n2 = random.randint(0,20)
        # operas = input(f'Введите операцию (+, -, /, *, mod, pow, div)')
        # allText = '+ - / * mod pow div'
        # lir = list ( map ( str , allText.split()))
        # operas = random.choice(lir)

poisnenie = ('Это программа калькулятор!\n'
'Основные правила:\n'
'Вводите арифметическое выражение со знаками без пробелов слитно в строчку\n'
'У вас три варинта выбора, кнопки на нлавеатуре 2, 3, 4, 5\n'
'--------------------------------------------------------------------------------------------------')
print('--------------------------')
print(poisnenie)

def reshenie1():
    count = 3
    for i in range(3):
        print('----------------------------')
        if count == 0: break 
        while True:
            try: 
                n1, operas, n2 = map(str, input(f'Введите 2 элемента и операцию (+, -, /, *, mod, pow, div)\nВвод: ')) 
                print(n1, operas, n2)
                n1 = int(n1) # переводим в целочисленные значения
                n2 = int(n2)
                while n1 < 0: 
                    n1, operas, n2 = map(str, input(f'Введите 2 элемента и операцию (+, -, /, *, mod, pow, div)\nВвод: ')) 
                    print(n1, operas, n2)      
                # if operas not in ["+", "-", "*", "/"]:
                #     raise ValueError
            except ValueError: print('Bad data passed.')
            else:      
                if operas == '%': operas = 'mod' # по заданию у нас должны быть такие выражения ниже, переводим
                elif operas == '**': operas = 'pow'
                elif operas == '//': operas = 'div'
                if operas == '+': print(n1 + n2)
                elif operas == '-': print(n1 - n2)
                elif operas == '*': print(n1 * n2)
                elif operas == '/': 
                    if n2 == 0: print("Деление на 0!")
                    else: print(n1 / n2)
                elif operas == 'mod': print(n1 % n2)
                elif operas == 'pow': print(n1 ** n2)
                elif operas == 'div': print(n1 // n2)
                # else: print('Неверная операция')
                count-=1
                print(f'Можно ввести еще {count} раза, после чего программа вернется в главное меню')
                if count == 0: return calkylator() 
                print('----------------------------')
    return operas

def reshenie2():
    count = 3
    for i in range(3):
        print('----------------------------')
        if count == 0: break 
        while True:
                try:            
                    n1, operas, n2, operas2, n3 = map(str, input(f'Введите 3 элемента и 2 операции (+, -, /, *, mod, pow, div)\nВвод: ')) 
                    n1 = int(n1) # переводим в целочисленные значения
                    n2 = int(n2)
                    n3 = int(n3)
                    while n1 < 0:               
                        n1, operas, n2, operas2, n3 = map(str, input('Введите корректное число\nВвод ')   ) 
                        print(n1, operas, n2, operas2, n3 )     
                except ValueError: print("Вы ввели не число. Повторите ввод")
                else:        
                    if operas == '%': operas = 'mod' # по заданию у нас должны быть такие выражения ниже, переводим
                    elif operas == '**': operas = 'pow'
                    elif operas == '//': operas = 'div'

                    if (operas == '+' and operas2 == '*') or (operas == '*' and operas2 == '+'): print(n1 + n2 * n3)
                    elif operas == '-' and operas2 == '*' : print(n1 - n2 * n3)
                    elif operas == '*' and operas2 == '-' : print(n1 * n2 - n3)
                    elif (operas == '+' and operas2 == '+') : print(n1 + n2 + n3)
                    elif (operas == '-' and operas2 == '-') : print(n1 - n2 - n3)
                    elif (operas == '+' and operas2 == '-') : print(n1 + n2 - n3)
                    elif (operas == '-' and operas2 == '+') : print(n1 - n2 + n3)
                    elif operas == '/' and operas2 == '*': 
                        if n2 == 0: print("Деление на 0!")
                        else: print(n1 / n2 * n3)
                    elif operas == '*' and operas2 == '/': 
                        if n2 == 0: print("Деление на 0!")
                        else: print(n1 * n2 / n3)
                    elif operas == '/' and operas2 == '-': 
                        if n2 == 0: print("Деление на 0!")
                        else: print(n1 / n2 - n3)
                    elif operas == '-' and operas2 == '/': 
                        if n2 == 0: print("Деление на 0!")
                        else: print(n1 - n2 / n3)
                    elif operas == '/' and operas2 == '+': 
                        if n2 == 0: print("Деление на 0!")
                        else: print(n1 / n2 + n3)
                    elif operas == '' and operas2 == '/': 
                        if n2 == 0: print("Деление на 0!")
                        else: print(n1 + n2 / n3)
                    elif operas == '/' and operas2 == '/': 
                        if n2 == 0: print("Деление на 0!")
                        else: print(n1 / n2 / n3)
                    elif operas == 'mod': print(n1 % n2)
                    elif operas == 'pow': print(n1 ** n2)
                    elif operas == 'div': print(n1 // n2)
                    # else: print('Неверная операция')
                    count-=1
                    print(f'Можно ввести еще {count} раза, после чего программа вернется в главное меню')
                    if count == 0: return calkylator()
                    print('----------------------------')
    return operas, operas2

def chislo():
    while True:
        expresion = ''
        count = 0
        for element in input():
            expresion += str(element)
            count = 0
            try:
                assert len(expresion) > 2  # если символов меньше двух вводится то заново набераем
                # print("Символов меньше 2, похоже ошибка")
                # assert all("a" <= i <= "z" for i in inp_str), print(
            except:    
                    count = 1 
            for i in expresion:
                    if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Я')\
                        or (i >= 'а' and i <= 'я') :
                        count = 1                         
        if count == 1: print(f'В уравнении не должно быть букв или некорректно')  
        else: return my_eval(expresion) 

import re
def my_eval(expresion):  
    actions = {
    "^": lambda x, y: str(float(x)**float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
    }

    priority_reg_exp = r"\((.+?)\)"
    action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
 
    while (match := re.search(priority_reg_exp, expresion)):
        expresion: str = expresion.replace(match.group(0), my_eval(match.group(1))) # рекурсия 
    for symbol, action in actions.items():
        while (match := re.search(action_reg_exp.format(symbol), expresion)):
            expresion: str = expresion.replace(match.group(0), action(*match.groups()))
            print(expresion) 
    return expresion 
   
    
def calkylator():
    import re
    while True:
        try:
            x = int(input('Выберите варианты уравнения с:\n (2)переменными [a+b]; (3)переменными [a+b+c]; (4)Много переменных [(a+b)*c/(d-g)] (5)Выход из программы\nВвод: '))
            while x <= 1 or x > 5:
                x = int(input('Введите корректное число')   ) 
        except ValueError: print("Вы ввели не число. Повторите ввод")
        else:
            while x != 5:
                if x == 2: 
                    print('2 переменные')
                    return reshenie1() 
                elif x == 3: 
                    print('3 переменные')
                    return reshenie2()
                elif x == 4: 
                    print('Много переменных + скобки')
                    return chislo()
            else: print ('выход из программы') 
            break                                     
calkylator()













#    expresion = ''
#                                 count = 0
#                                 for element in input():
#                                     expresion += str(element)
#                                     expresion = re.compile("[^\d+]{1}")





 # \( - Для проверки наличия скобки в тексте, внутри символ от 1 до бесконечности возможно, кпроверка закрывающейся скобки

#  шпаргалка https://chel-center.ru/python-yfc/2020/04/28/shpargalka-po-regulyarnym-vyrazheniyam/?ysclid=l65op4obir47173089

# -?\d+  - возможный минус десятичная цифра любого размера от 1, 
# (?:\.\d+)? возможно скобка открывается, : точка после десятичная цифра любого размера от 1, возможно скобка закрывается
# это похоже на вещественные числа, это первое выражение (-?\d+(?:\.\d+)?)
# \s*\{}\s* - пробельный символ, от 0 или более вхождений в заданном количестве, пробельный символ от 0 или более вхождений
# один в один повторяется прежнее уравнение (-?\d+(?:\.\d+)?)
       


# exp = "(1 + 4) * (5 * (10 - 2)) / 5"
# my_eval(expresion), eval(expresion) # 40.0 40.0


# g = [y := f(3), y**2, y**3] #содержимое: [5, 25, 125]
# := это равернство которое присваивает значение прямо внутри строки
# или нужно было делать так
# y = f(3)
# g = [y, y**2, y**3]
    # Оператор := может использоваться для присвоения переменных во время вычисления другого выражения.








