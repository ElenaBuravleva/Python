import matplotlib.pyplot as plt
import numpy as np


def task1():
    fig, ax = plt.subplots()
    ax.set_title('График функции y = 5x2 + 10x - 30')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    x_cords = np.linspace(-100, 100) 
    y_cords = [5*x*x + 10*x - 30 for x in x_cords]
    ax.plot(x_cords, y_cords)
    plt.show()
task1()
#Имеются данные о площади и стоимости 15 домов.
#Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
#Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список подходящих ему домов, отсортированных по площади.
def task2():
    import random
    fig, ax = plt.subplots()
    fig, nx = plt.subplots()
    ax.plot(100)
    ax.set_title('Cтоимость квадратного метра площади каждого дома')
    ax.set_xlabel('Номер дома')
    ax.set_ylabel('Цена за м2, тыс. руб.')
    areas = list(random.randint(100,300) for _ in range(15))
    prices = list(random.randint(30,200)/10 for _ in range(15))
    house_dict = {}
    for i in range(1,16):
        number = i
        price_m2 = prices[i-1]*1000/areas[i-1]
        if price_m2 < 50:
            house_dict[i] = areas[i-1],price_m2
        ax.scatter(number,price_m2)
    elements_sorted = {k: house_dict[k] for k in sorted(house_dict, key=house_dict.get)}
    for v in elements_sorted.values():
        nx.scatter(v[1],v[0],  color='red')
    ax.grid()
    nx.plot(50)
    nx.set_title('Подходящие дома, кв.м. в которых стоит менее 50 тыс. руб.')
    nx.set_xlabel('Цена за м2, тыс. руб.')
    nx.set_ylabel('Площадь дома, м2')
    nx.grid()
    plt.show()
task2()