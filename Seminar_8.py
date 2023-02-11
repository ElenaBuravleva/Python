#Задача 1
def task1():
    print('Программа, определяющая группу с наилучшим средним баллом')
    import random
    count = random.randint(5 ,10)
    print(f'Табели  {count} групп:')
    tabel = [0] * count
    number = 0
    for i in range(count):
        tabel[i] = [random.randint(2,5) for _ in range(random.randint(20, 30))]
    for row in tabel:
        number += 1
        print(f'Группа №{number}: {row}')
    max = 0
    number = 0
    for i in range(count):
        score = 0
        students_count = len(tabel[i])
        for j in range(students_count):
            score += tabel[i][j]
        score /= students_count
        if score > max:
            max = score
            number = i + 1
    print(f'Группа с наилучшим средним баллом: № {number}')
task1()

def task2():
    import random
    flag = False
    print('Программа, определяющая сумма элементов каких строк превосходит сумму главной диагонали квадратной матрицы')
    rows = int(input('Введите размер матрицы: '))
    array = [0] * rows
    for i in range(rows):
        array[i] = [random.randint(1,100) for _ in range(rows)]
    for row in array:
        print(row)
    diagonal_sum = 0
    for i in range(rows):
        diagonal_sum += array[i][i]
    for j in range(rows):
        row_sum = sum(array[j])
        if row_sum > diagonal_sum:
            print(f'Cумма элементов {j + 1} строки превосходит сумму главной диагонали {row_sum} > {diagonal_sum}')
            flag = True
    if flag == False:
        print(f'В матрице нет строк, сумма элементов которых превосходит сумму главной диагонали {diagonal_sum}')
task2()

def determine_period(month, name):
    week = 7
    max = 0
    date_max = 1
    min = 1000
    date_min = 1
    print(name)
    for day in range(len(month) - 1 - week):
        week_t = month[day:day + week]
        sum_temp = sum(week_t)
        if sum_temp > max:
            max = sum_temp
            date_max = day
        elif sum_temp < min:
            min = sum_temp
            date_min = day
    print(f'Cамый жаркий период c {date_max + 1} по {date_max + week}. Средняя температура составила {round(max/week, 1)}')
    print(f'Cамый холодный период c {date_min + 1} по {date_min + week}. Средняя температура составила {round(min/week, 1)}')

def task3():
    print('Программа, определяющая самый жаркий и самый холодный 7-дневный промежуток месяца.\nЕсть данные с мая по сентябрь:')
    import random
    for i in range(5):
        if i == 0:
            count_days = 31
            min_temp = 5
            max_temp = 30
            name = 'Май'
        elif i == 1:
            count_days = 31
            min_temp = 10
            max_temp = 30
            name = 'Июнь'
        elif i == 4:    
            count_days = 30
            min_temp = 3
            max_temp = 27
            name = 'Сентябрь'
        else:
            count_days = 31
            min_temp = 15
            max_temp = 36
            if i == 2:
                name = 'Июль'
            else:
                name = 'Август'
        array_temp = [random.randint(min_temp, max_temp) for _ in range(count_days)]
        determine_period(array_temp, name)
task3()
        
