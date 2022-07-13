# КНБ - вы играете с ботом, варианты раунда игры - победа 1 очко, проигрыш 0 очков, ничья 0.5 балла
# играть неограниченное количетсво раундов и вся статистика созранялась





















import random



a = input('введите К или Н или Б (либо q для выхода): ')

result1 = 0
result2 = 0

# def knb(a):
# 	global result1, result2
#
# 	if a == 'q':
# 		print(result1, result2)
# 	else:
# 		while


x = random.randint(0, 3)

while True:
	x = random.randint(0, 3)
	if x != 'q':
		if x == 0:
			if a == 'К':
				result1 += 0
				result2 += 0
			if a == 'Н':
				result1 += 1
				result2 += 0
			if a == 'Б':
				result1 += 0
				result2 += 1
		if x == 1:
			if a == 'К':
				result1 += 0
				result2 += 1
			if a == 'Н':
				result1 += 0
				result2 += 0
			if a == 'Б':
				result1 += 1
				result2 += 0
		if x == 2:
			if a == 'К':
				result1 += 1
				result2 += 0
			if a == 'Н':
				result1 += 0
				result2 += 1
			if a == 'Б':
				result1 += 0
				result2 += 0
		else:
			break
print(result1, result2)
