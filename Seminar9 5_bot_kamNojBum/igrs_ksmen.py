import random

def igra():
    result1 = 0
    result2 = 0
        
    status = True
    while status != False:

        for i in range(5):

            player1 = input(f'Выберите камень(1) ножницы(2) бумагу(3)\n')	

            znach = 'k n b'
            lir = list ( map ( str , znach.split()))
            player2 = random.choice(lir)

            if player2 == 'k': player2 = "камень"  # замена
            elif player2 == 'n': player2 = "ножницы"
            elif player2 == 'b': player2 = "бумагу"

            if player1 == '1': player1 = 'камень' # очень важно присвоить значение =, а не равно
            elif player1 == '2': player1 = 'ножницы'
            elif player1 == '3': player1 = 'бумагу'

            print(f'Я выбрал {player1}: ')
            print(f'player2 выбрал {player2}: ')


            if player1 == 'камень': player1 = 'k' # замена
            elif player1 == 'ножницы': player1 = 'n'
            elif player1 == 'бумагу': player1 = 'b'

            if player2 == "камень": player2 = 'k'
            elif player2 == "ножницы": player2 = 'n'
            elif player2 == "бумагу": player2 = 'b'


            if player1 == 'k' and player2 == 'k':
                result1 += 0.5
                result2 += 0.5
                print(f'ничья;  общий счет: {result1}:{result2}' )
            elif player1 == 'k' and player2 == 'n':
                result1 += 1
                result2 += 0
                print(f'победил player1;  общий счет: {result1}:{result2}')
            elif player1 == 'k' and player2 == 'b':
                result1 += 0
                result2 += 1
                print(f'победил player2;  общий счет: {result1}:{result2}')
            elif player1 == 'n' and player2 == 'k':
                result1 += 0
                result2 += 1
                print(f'победил player2;  общий счет: {result1}:{result2}')
            elif player1 == 'n' and player2 == 'n':
                result1 += 0.5
                result2 += 0.5
                print(f'ничья;  общий счет: {result1}:{result2}')
            elif player1 == 'n' and player2 == 'b':
                result1 += 0
                result2 += 1
                print(f'победил player2;  общий счет: {result1}:{result2}')
            elif player1 == 'b' and player2 == 'k':
                result1 += 1
                result2 += 0
                print(f'победил player1;  общий счет: {result1}:{result2}')
            elif player1 == 'b' and player2 == 'b':
                result1 += 0.5
                result2 += 0.5
                print(f'ничья;  общий счет: {result1}:{result2}')
            elif player1 == 'b' and player2 == 'n':
                result1 += 0
                result2 += 1
                print(f'победил player2;  общий счет: {result1}:{result2}')
            else:
                print(f'общий счет {result1}:{result2}   выберите клавиши 1 2 3 ')

        status = input('Введите "q", чтобы выйти из игры.')
        if status == 'q' or status == 'quit':
            status = False
    return result1, result2
igra()