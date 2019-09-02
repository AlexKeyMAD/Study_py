import os

os.system('cls')

print('Переводчик с римской системы исчисления в арабскую.')

tab_rome_arab_num = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}

def resulting_number(str_num):

    return_number = tab_rome_arab_num.get(str_num,0)

    if return_number == 0:
        print(f'Символ {str_num} не соответствует римской системе исчисления')

    return return_number

def pars_numbers(rome_num):

    num = 0
    list_num = []
    str_len = len(rome_num)

    while num < str_len:

        a = resulting_number(rome_num[num])

        if num + 1 == str_len:
            b = 0
        else:
            b = resulting_number(rome_num[num + 1])
        
        if a < b:
            list_num.append(-a)
        else:
            list_num.append(a)        
        
        num += 1

    return sum(list_num)

def exchange_numbers(rome_num):

    arab_num = pars_numbers(rome_num)
    
    print(f'Римское число {rome_num} - это {arab_num} по арабски')

input_number = input('Введите римские цифры: ')

exchange_numbers(input_number)