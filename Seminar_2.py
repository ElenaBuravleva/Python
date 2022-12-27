# Задача 1.
def zadacha1():
    print('Программа, транслирующая список факториалов для чисел  от 1 до заданного N')
    number = int(input('Введите положительное число N = '))
    if number == 0:
        print('[1]')
    elif number > 0:
        print('[',end='')
        for posfactorial in range(1,number + 1):
            factorial = 1
            for index in range(1,posfactorial + 1):
                factorial = factorial*index
            if posfactorial != number:
                print(factorial, end=',')
            else:
                print(f'{factorial}]')
    else:
        print('Факториал отрицательного числа не существует')
zadacha1()
#Задача 2. 
def zadacha2():
    print('Таблица истинности для выражения ¬(X ∧ Y) ∨ Z')
    print ('X  Y  Z ¬(X∧Y)∨Z')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print (f'{x}  {y}  {z}  {int((not(x and y))or z)}')
zadacha2()
#Задача 3. 
def zadacha3():
    print('Программа подсчёта символов первой строки, встречающихся во второй')
    firststring = input('Введите набор символов первой строки  ')
    secondstring = input('Введите набор символов второй строки ')
    for i in range(len(firststring)):
        countletter = 0
        for j in range(len(secondstring)):
            if firststring[i] == secondstring[j]:
                countletter += 1
        if countletter == 0:
            print(f'Символ {firststring[i]} не встречается во второй строке')
        else:
            print(f'Символ {firststring[i]} встречается во второй строке {countletter} раз(a)')
zadacha3()
#Задача 4. 
def zadacha4():
    print('Сдвиг элементов списка, заполненного числами из промежутка [-N, N] на 2 позиции вправо')
    number = int(input('Введите число N = '))
    list = []
    for i in range(-number,number + 1):
        list.append(i)
    print(list,end= ' -> ')
    list1 = list[-2:]
    list2 = list[:-2]
    for j in range(len(list2)):
        list1.append(list2[j])
    print(list1)
zadacha4()