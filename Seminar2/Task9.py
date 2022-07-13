# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# предикат это True = 1 и False = 0, значения истинности


x = 1
y = 1
z = 0
def truth_check(x,y,z):
    left = not (x or y or z) # если  false
    right = not x and not y and not z # если false
    result = left == right
    return result
print(truth_check(x,y,z)) # True




# Обозначения логических операций
# И (AND): & • ∧ *
# ИЛИ (OR): ∨ +
# НЕ (NOT): ¬ !
# Исключающее ИЛИ (XOR): ⊕ ^
# Импликация: -> → =>
# Эквивалентность: = ~ ≡ <=>
# Штрих Шеффера: ↑ |
# Стрелка Пирса: ↓


def sravn(x,y,z):
    if not(x or y or z) == ((not x) and (not y) and (not z)):
        return True
    else: return False

marker = True
for i in False, True:
    for j in False, True:
        for k in False, True:
            if sravn(i,j,k) != True:
                marker = False
print(marker)

print(sravn(True,False,True)) # 1 0 1  = 1