# 2.Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# Обозначения логических операций
# И (AND): & • ∧ *
# ИЛИ (OR): ∨ +
# НЕ (NOT): ¬ !
# Исключающее ИЛИ (XOR): ⊕ ^
# Импликация: -> → =>
# Эквивалентность: = ~ ≡ <=>
# Штрих Шеффера: ↑ |
# Стрелка Пирса: ↓


x = 0
y = 1
z = 1
def truth_check(x,y,z):
    left = not (x or y or z)
    right = not x and not y and not z
    result = left == right
    return result
print(truth_check(x,y,z))