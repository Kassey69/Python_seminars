


 

# def my_eval():
#     expresion = ''
#     for element in input():
#         expresion += str(element)

#     actions = {
#     "^": lambda x, y: str(float(x)**float(y)),
#     "*": lambda x, y: str(float(x) * float(y)),
#     "/": lambda x, y: str(float(x) / float(y)),
#     "+": lambda x, y: str(float(x) + float(y)),
#     "-": lambda x, y: str(float(x) - float(y))
#     }   

#     priority_reg_exp = r"\((.+?)\)"
#     action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)" 
 

#     while (match := re.search(priority_reg_exp, expresion)):
#         expresion: str = expresion.replace(match.group(0), (match.group(1)))
 
#     for symbol, action in actions.items():
#         while (match := re.search(action_reg_exp.format(symbol), expresion)):
#             expresion: str = expresion.replace(match.group(0), action(*match.groups()))

#         print((expresion))  
#     return expresion
# my_eval()




# # g = [y := f(3), y**2, y**3] #содержимое: [5, 25, 125]
# # := это равернство которое присваивает значение прямо внутри строки
# # или нужно было делать так
# # y = f(3)
# # g = [y, y**2, y**3]
#     # Оператор := может использоваться для присвоения переменных во время вычисления другого выражения.


import re

def eshenie3():
    expresion = ''
    for element in input():
        expresion += str(element)
    return expresion
  
yravn = eshenie3()

def my_eval(expresion: str) -> str:
    # global yravn
    # yravn = eshenie3()
    
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

my_eval(yravn)
 
# exp = "(1 + 4) * (5 * (10 - 2)) / 5"
# my_eval(expresion), eval(expresion) # 40.0 40.0