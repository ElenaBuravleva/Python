def task1():
    import random
    print('Программа вывода из списка случайных чисел от 1 до 10 тех элементов, которые больше 5')
    numbers = list(random.randint(1,10) for _ in range(10))
    print (f'Случайные числа: {numbers} -> {list(filter(lambda x: x > 5, numbers))}')
task1()

def task2():
    import random
    print('Программа вывода из списка случайных чисел от 1 до 10 случайных возрастающих последовательностей')
    numbers = list(random.randint(1,10) for _ in range(random.randint(10,20)))
    random_element = random.randint(0, len(numbers) - 1)
    random_result = [numbers[random_element]]
    while random_element < len(numbers):
        random_element = random.randint(random_element, len(numbers))
        if random_element != len(numbers) and numbers[random_element] > random_result[-1]:
            random_result.append(numbers[random_element])
    print (f'Список случайных чисел: {numbers} -> {random_result}')
task2()

def task3():
    import random
    print('Программа подсчета совпадающих элементов списка случайных чисел от 1 до 10 и выдачи списка уникальных элементов')
    numbers = list(random.randint(1,10) for _ in range(random.randint(5,10)))
    print (f'Список уникальных значений: {set(numbers)}')
    result = list(filter(lambda x: numbers.count(x) > 1, numbers))
    print(f'Совпадающие элементы:{result}')
    result = list(map(lambda x: numbers.count(x) > 1, numbers))
    print (f'{numbers} => {result.count(True)} (a/ов) совпадают')
task3()