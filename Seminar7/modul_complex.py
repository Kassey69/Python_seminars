import math
import cmath # импорт комплексной математики

# В основе комплексных чисел лежит величина j = sqrt(-1)
# если представить я в виде суммы вещественной части ву виде 
# z = x + y*j, где x и y вещественные числа 
# любая математическая qeyrwbz от комплексного числа все равно возвращает комплексное число

# в питоне зашиты комплексные числа 

















# import re

# def my_eval(expresion):
    
#     actions = {  
#     "^": lambda x, y: str(float(x) ** float(y)),
#     "*": lambda x, y: str(float(x) * float(y)),
#     "/": lambda x, y: str(float(x) / float(y)),
#     "+": lambda x, y: str((float(x) + str('i')) + (float(y) + str('i'))),
#     "-": lambda x, y:  str((float(x) + ('i')) - (float(y) + ('i'))),
#     "%": lambda x, y: str(float(x) % float(y)),
#     "//": lambda x, y: str(float(x) // float(y)),
#     "//": lambda x, y: str(float(x) // float(y)),
#     }
    
#     priority_reg_exp = r"\((.+?)\)"
#     action_reg_exp = r"(-?\d+[i]?(?:\.\d+[i]?)?)\s*\{}\s*(-?\d+[i]?(?:\.\d+[i]?)?)"

 
#     while (match := re.search(priority_reg_exp, expresion)): # поиск подстроки в строке
#         expresion: str = expresion.replace(match.group(0), my_eval(match.group(1))) # рекурсия
    
#     for symbol, action in actions.items():
#         while (match := re.search(action_reg_exp.format(symbol), expresion)):
#             expresion: str = expresion.replace(match.group(0), action(*match.groups()))
#             print(expresion)
#     return expresion
