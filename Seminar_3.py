#Задача 1. 
def fibonachi():
    print('Программа, записывающая в файл N первых элементов последовательности Фибоначчи.')
    fib1 = 0
    fib2 = 1
    N = int(input("Введите число элементов ряда Фибоначчи: "))
    index = 0
    serias = ' '
    while index < N:
        pair_sum = fib1 + fib2
        serias = str(fib2)
        fib1 = fib2
        fib2 = pair_sum
        index += 1
        with open('fibonachi.txt','a',encoding='utf-8') as datafibonachi:
            datafibonachi.write(serias)
            datafibonachi.write(' ')
    with open('fibonachi.txt','a',encoding='utf-8') as datafibonachi:
        datafibonachi.write('\n')
    print('Проверьте файл fibonachi.txt. Там появилась новая запись.')
fibonachi() 
#Задача 2. В файле находятся  фруктов. 
def fruits():
    print('Программа, которая выводит все фрукты, названия которых начинаются на заданную букву')
    letter = input("Введите букву: ")
    data = open('fruit.txt',encoding='utf-8')
    names = data.readlines()
    data.close()
    for i in range (1,len(names)):
        fruit = names[i]
        if fruit[0] == letter:
            print(names[i])
fruits()       
#Задача 3. 
# Вариант 1: новые фразы дополняются в первоначальный словарь из трёх фраз.
def bot():
    print('Бот, который находит ответы на фразы по ключу в словаре')
    dictionary = {
        'Привет!': 'Добрый день!',
        'Как тебя зовут?': 'Меня зовут Анатолий.',
        'Пока!': 'До свидания!'
        }
    indicator = 0
    while indicator != 2:
        phrase = input('Вы: ')
        newkey = dictionary.setdefault(phrase)
        if dictionary[phrase] != None:
            print(f'Бот: {dictionary[phrase]}')
            if phrase == 'Пока!':
                indicator = 2
        else:
            print('Бот: Я Вас не понимаю!')
            dictionary[phrase] = input('Напишите, что я должен был ответить: ')
bot()
#Задача 3.
# Вариант 2: Есть 2 файла: в одном - обращения, в другом - ответы, все новые фразы записываются в файлы.
def bot1():
    dictionary = { }
    data = open('textbot.txt','r', encoding='utf-8')
    list = []
    for line in data:
        list.append(line[:-1])
    data.close()
    print('С этими фразами уже можно обращаться к боту:')
    print(list)
    data = open('answer.txt','r', encoding='utf-8')
    list2 = []
    for line in data:
        list2.append(line[:-1])
    data.close()
    for i in range(len(list)):
        dictionary.setdefault(list[i])
        dictionary[list[i]] = list2[i]
    indicator = 0
    while indicator != 2:
        phrase = input('Вы: ')
        newkey = dictionary.setdefault(phrase)
        if dictionary[phrase] != None:
            print(f'Бот: {dictionary[phrase]}')
            if phrase == 'Пока!':
                indicator = 2
        else:
            print('Бот: Я Вас не понимаю!')
            with open('textbot.txt','a',encoding='utf-8') as newdata:
                newdata.writelines(f'\n{phrase}')
            newvalue = input('Напишите, что я должен был ответить: ')
            dictionary[phrase] = newvalue
            with open('answer.txt','a',encoding='utf-8') as newdata1:
                newdata1.writelines(f'\n{newvalue}')
bot1()