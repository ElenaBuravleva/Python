# Задача 4.
print('Программа, которая на вход принимает число N, а на выходе показывает все чётные числа от 1 до N')
number = int(input('Введите положительное число '))
if number < 0:
    print('Вы ввели отрицательное число')
elif number <= 1:
    print('Четных чисел нет')
else:
    print('Четные числа: ',end=' ')
    count = 2
    while count <= number:
        print(count,end=' ')
        count = count + 2