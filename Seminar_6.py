def task1():
    print('Программа нахождения значения выражения: N + NN + NNN при заданном N')
    number = input('Введите натуральное число N: ')
    print(int(number*2) + int(number*2) + int(number))
task1()

def task2():
    print('Программа, определяеющая, есть ли в массиве из 15 элементов последовательность из трёх элементов, совпадающая с введённым числом')
    import random
    array_numbers = [random.randint(0,9) for _ in range(15)] 
    #array_numbers = [1,3,2,4,5,1,0,3,5,9,9,9,9,8,7]
    number = int(input('Введите трёхзначное натуральное число: '))
    if number > 999 or number < 100:
        number = int(input('Число должно быть трёхзначным: '))
    result = ' '
    for num in array_numbers:
        result += str(num)
    if str(number) in result:
        print(f'В последовательности {array_numbers} есть число {number}')
    else:
        print(f'В последовательности {array_numbers} нет совпадений с введенным числом {number}')
task2()

def find_csd(num, den):
    scd = 1
    for number in (range(2, den + 1)):
        if num % number == 0 and den % number == 0:
            scd = number
           # print(scd)
            break
    return scd == 1


def task3():
    print('Программа нахождения всех простых несократимых дробей между 0 и 1 со знаменателем < 11')
    for den in range(1,12):
        print()
        for num in range(1,den):
            if find_csd(num, den):
                print(f'{num}/{den}', end=' ')
            
task3()