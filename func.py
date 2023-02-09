def print_last_row():
    data = open('text.txt',encoding='utf-8')# Можно русский язык считывать
    print(data)
    text = data.readlines()
    print(text[-1])

def read_odd_rows():
    data = open('task1.txt',encoding='utf-8')
    text = data.readlines()
    data.close()
    for i in range (0,len(text),2):
        print(text[i])

def read_even_rows():
    data = open('task1.txt',encoding='utf-8')
    text = data.readlines()
    data.close()
    for i in range (1,len(text),2):
        print(text[i])
def generation(): #генерирует пароль и пишет в файл
    lenpass = int(input('Введите длину пароля '))
    import random
    data = open('task3.txt',encoding='utf-8')
    symbols = data.readline()
    data.close()
    password = ' '
    for index in range(lenpass):
        number_element = random.randint(0,len(symbols)- 1)
        password += symbols[number_element]
    print(password)
    with open('password.txt','w',encoding='utf-8') as newdata:
       newdata.write(password)
#    with open('password.txt','a',encoding='utf-8') as newdata:# Будет дозаписывать в тот же файл
 #       newdata.write(password + '\n')
    print(f'Пароль создан!')

def poem():
    data = open('task4.txt',encoding='utf-8')
    text = data.read()
    print(text)
    data.close()
    dictionary = {}
    for letter in text:
        dictionary[letter] = letter
    for el in dictionary:
        print(el, end=' ')
poem()