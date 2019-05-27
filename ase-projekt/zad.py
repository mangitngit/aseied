from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
import numpy as np
import matplotlib.pyplot as plt
import random
from math import *

def spark():
    sc = SparkContext('local', 'ap')
    sqlContext = SQLContext(sc)
    df = sqlContext.read.json('data.json', multiLine=True)

    data = df.select('data')
    return np.array(data.first().__getitem__('data'))


def apriori(A, B):      # prawdopodobienstwo apriori
    sum = A + B
    A_apriori = A/sum
    B_apriori = B/sum
    return A_apriori, B_apriori


def naive_bayes(data, point, possible):
    nearest = []
    for po in data:
        nearest_point = sqrt((point[0]-po[0])**2 + (point[1]-po[1])**2)
        nearest.append([po[2], nearest_point])      # tablica z kolorami i odległościami od punktów
    nearest.sort(key=lambda near: near[1])          # posortowanie tablicy względem odległości

    A_possible = 0
    B_possible = 0

    for x in range(5):              # liczenie kolorów pięciu najbliższych punktów
        if nearest[x][0] == 'g':
            A_possible += 1
        if nearest[x][0] == 'r':
            B_possible += 1

    A_chanse = possible[2] * (A_possible / possible[0])     # szanse na wystąpienie danego koloru
    B_chanse = possible[3] * (B_possible / possible[1])

    if A_chanse > B_chanse:         # zwrócenie bardziej prawdopodobnego koloru punktu
        possible[0] += 1            # ponowne obliczenie prawdopodobieństw apriori
        possible[2], possible[3] = apriori(possible[0], possible[1])
        return 'g'
    else:
        possible[1] += 1
        possible[2], possible[3] = apriori(possible[0], possible[1])
        return 'r'


def ploting_dot(x, y, color):       # rysowanie białej kropki
    plt.scatter(x, y, facecolors='none', edgecolors='k')
    plt.pause(0.4)
    plt.scatter(x, y, s=50, facecolors=color)       # po odstępie czasowym zastapienie jej kolorem
    plt.draw()


def onclick(event):                  # event kliknięcia na pyplot
    x = random.uniform(5, 40)         # losowanie punktu
    y = random.uniform(5, 40)
    color = naive_bayes(points, [x, y], possible)     # prawdopodobny kolor
    points.append([x, y, color])                      # uaktualnienie bazy
    ploting_dot(x, y, color)


def ploting(data):
    fig, ax = plt.subplots()            # ustawienia plotu
    cid = fig.canvas.mpl_connect('button_press_event', onclick)

    for point in data:              # rysowanie początkowych punktów
        plt.scatter(point[0], point[1], s=50,  facecolors=point[2])


temporary_points = spark()
points = []

for point in temporary_points:
    points.append([point[0], point[1], 'g'])
    points.append([point[2], point[3], 'r'])

A_amount, B_amount = 100, 100
A_apriori, B_apriori = apriori(A_amount, B_amount)
possible = [A_amount, B_amount, A_apriori, B_apriori]

ploting(points)

plt.show()