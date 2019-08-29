import random

our_number = random.randint(1,50)

life = 0

print('Игра "Угадай число"')

while life < 6:
    
    life+=1

    user_number = int(input('Введите число от 1 до 50:'))

    if user_number == our_number:
        print(f'Число угадано, за {life} попыток')
        break
    else:
        if user_number > our_number:
            print('Число больше загаданного')
        else:
            print('Число меньше загаданного')

    if life == 6:
        print(f'Число не угадано за 6 попыток. Game Over. Загаданное число: {our_number}')
        break