print('Игра "Крестики-нолики"')

batlle_field = {str(a):str(a) for a in range(9)}

win_list = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

def print_batlle_field():
    text = ''
    a = 0
    while a != 9:
        text += f' {batlle_field[str(a)]}'
        if a == 2 or a == 5 or a == 8:
            print(text)
            text = ''
        a += 1

def checking_for_correct_input(value):
    
    try:
        int_value = int(value)
    except:
        print('Введенное вами значение не число!')
        return False
    
    if int_value < 0 or int_value > 8:
        print('Введенное число должно быть от 0 до 8')
        return False
        
    field = batlle_field[value]
    if field == 'X' or field == 'O':
        print(f'В ячейку {value} нельзя ставить крестик или нолик, ячейка уже занята')
        return False
    
    return True

def checking_for_victory(player):
    
    for it in win_list:
        s = 0
        for value in it:
            if batlle_field[str(value)] == player:
                s += 1
        
        if s == 3:
            print(f'Победа игрока играющего "{player}"')
            return True
        
    return False

print_batlle_field()

list_players = ['X','O']

level = 0

while level != 9:
        
    for player in list_players:
        
        level += 1
        
        cor_val = False
        cell = 0
        while cor_val == False:
            cell = input(f'В какую ячейку поставите "{player}"?: ')
            cor_val = checking_for_correct_input(cell)
            
        batlle_field[cell] = player
        print_batlle_field()
        
        if checking_for_victory(player) == True or level == 9:
            level = 9
            print('Игра окончена')
            break    