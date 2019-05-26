import matplotlib.pyplot as plt
import random
import numpy as np
from math import *

"""
Dodajemy nowe kropki poprzez naciśnięcie myszki na plot
A - green
B - red
"""


def read(link, color):          # wczytanie danych
    file = open(link, 'r')
    points_data = []
    amount = 0
    for line in file:
        amount += 1
        line = line.replace(',', '.').rstrip()
        split = line.split('|', 1)
        points_data.append([float(split[0]), float(split[1]), color])
    return points_data, amount


def apriori(a, b):      # prawdopodobienstwo apriori
    sum_ab = a + b
    a_apriori = a / sum_ab
    b_apriori = b / sum_ab
    return a_apriori, b_apriori


def naive_bayes(points_data, points, if_possible):
    nearest = []
    for po in points_data:
        nearest_point = sqrt((points[0] - po[0]) ** 2 + (points[1] - po[1]) ** 2)
        nearest.append([po[2], nearest_point])      # tablica z kolorami i odległościami od punktów
    nearest.sort(key=lambda near: near[1])          # posortowanie tablicy względem odległości

    a_possible = 0
    b_possible = 0

    for x in range(5):              # liczenie kolorów pięciu najbliższych punktów
        if nearest[x][0] == 'g':
            a_possible += 1
        if nearest[x][0] == 'r':
            b_possible += 1

    a_chanse = if_possible[2] * (a_possible / if_possible[0])     # szanse na wystąpienie danego koloru
    b_chanse = if_possible[3] * (b_possible / if_possible[1])

    if a_chanse > b_chanse:         # zwrócenie bardziej prawdopodobnego koloru punktu
        if_possible[0] += 1            # ponowne obliczenie prawdopodobieństw apriori
        if_possible[2], if_possible[3] = apriori(if_possible[0], if_possible[1])
        return 'g'
    else:
        if_possible[1] += 1
        if_possible[2], if_possible[3] = apriori(if_possible[0], if_possible[1])
        return 'r'


def ploting_dot(x, y, color):       # rysowanie białej kropki
    plt.scatter(x, y, facecolors='none', edgecolors='k')
    plt.pause(0.4)
    plt.scatter(x, y, s=50, facecolors=color)       # po odstępie czasowym zastapienie jej kolorem
    plt.draw()


def onclick(event):                  # event kliknięcia na pyplot
    x = random.uniform(0, 2)         # losowanie punktu
    y = random.uniform(2, 6)
    color = naive_bayes(data, [x, y], possible)     # prawdopodobny kolor
    data.append([x, y, color])                      # uaktualnienie bazy
    ploting_dot(x, y, color)


def ploting(points_data):
    fig, ax = plt.subplots()            # ustawienia plotu
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.xticks(np.arange(-0.5, 3.5, 1.0))
    plt.yticks(np.arange(0.5, 7.5, 1.0))
    ax.set_yticklabels([])
    ax.set_xticklabels([])

    for points in points_data:              # rysowanie początkowych punktów
        plt.scatter(points[0], points[1], s=50, facecolors=points[2])


A, A_amount = read('data/data1.csv', 'g')
B, B_amount = read('data/data2.csv', 'r')
data = A
for point in B:     # połeczenie danych A i B
    data.append(point)

A_apriori, B_apriori = apriori(A_amount, B_amount)
possible = [A_amount, B_amount, A_apriori, B_apriori]

ploting(data)

plt.show()
