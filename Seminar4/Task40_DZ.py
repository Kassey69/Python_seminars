# Вычислить число c заданной точностью d
# Вычислить результат деления двух чисел c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
import random

p = math.pi
print(f'pi =',(p)) # pi = 3.141592653589793
print(f'pi =',round(p,3)) # 3.142
print("")

def accuracy():
    a = random.uniform(1,100)
    b = random.uniform(1,100)
    print(f'[{a} / {b} = {a / b}]')
    res = a / b
    print(f'[{round(a,3)} / {round(b,3)} = {round(a / b,3)}]')
    return [round(res,3)]

result = accuracy()
print(f'Результат деления двух чисел c заданной точностью:',result) # 2.422