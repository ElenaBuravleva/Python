def task1():
    print('Программа вывода списка простых множителей числа N')
    N = int(input("Введите натуральное число N: "))
    if N < 1:
        N = int(input("Натуральные числа - целое положительные числа, отличные от 0. Введите натуральное число N: "))
    else:
        result = []
        for i in range(2, N + 1):
            if N != 1:
                while N % i == 0:
                    result.append(i)
                    N = N // i
        print(result)
task1()

def ice_cream():
    print('Программа вывода отсутствующего товара')
    data = open('ice cream.txt', mode = 'r', encoding='utf-8')
    names = data.readlines()
    data.close()
    avail = set(names[0].removesuffix('\n').split(', '))
    absence = set(names[1].removesuffix('\n').split(', '))
    print(f'Отсутствует: {avail.difference(absence)}')
ice_cream()

def round_pi():
    import math
    print('Программа вывода числа Пи с заданной точностью')
    ndp = int(input('Введите требуемое количество знаков после ",": '))
    print(round(math.pi, ndp))
round_pi()

def converting(polynom):#достает коэффициенты многочлена
    polynom = polynom[0].replace('= 0', '').split(' + ')
    polynom = [member[0] for member in polynom]
    for i in range(len(polynom)):
        if polynom[i] == 'x':
            polynom[i] = '1'
    if len(polynom) < 3:
        polynom.append(0)
    return polynom

def task4():
    print('Программа сложения многочленов')
    data = open('polynom1.txt', mode = 'r', encoding='utf-8')
    polynom1 = data.readlines()
    data.close()
    data = open('polynom2.txt', mode = 'r', encoding='utf-8')
    polynom2 = data.readlines()
    data.close()
    
    polysum = []
    for i in range(3):
        polysum.append(int(converting(polynom1)[i]) + int(converting(polynom2)[i])) 
    print(f'{polynom1} + {polynom2} = {polysum[0]}x^2 + {polysum[1]}x + {polysum[2]}')
task4()