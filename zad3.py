import random
import time


def bubble_sort(sort):                      # sortowanie bąbelkowe
    start = time.time()
    while True:
        list_sorted = False
        for i in range(len(sort)-1, 0, -1):
            if sort[i] < sort[i-1]:
                sort[i], sort[i-1] = sort[i-1], sort[i]
                list_sorted = True
        if not list_sorted:
            break
    end = time.time()
    operation_time = end - start
    print("bubble sort time =    ", round(operation_time, 5))
    return sort


def selection_sort(sort):                   # sortowanie przez wybór
    start = time.time()
    n = 0
    while n < len(sort):
        min_value = max_rand + 1
        min_id = n
        for i in range(n, len(sort)):
            if min_value > sort[i]:
                min_value = sort[i]
                min_id = i
        sort[n], sort[min_id] = sort[min_id], sort[n]
        n += 1
    end = time.time()
    operation_time = end - start
    print("selection sort time = ", round(operation_time, 5))
    return sort


def quick(sort):                             # sortowanie szybkie
    if len(sort) < 2:
        return sort
    pivot = len(sort)//2
    left = [x for x in sort[:pivot] + sort[pivot+1:] if x < sort[pivot]]
    right = [x for x in sort[:pivot] + sort[pivot+1:] if x >= sort[pivot]]
    return quick(left) + [sort[pivot]] + quick(right)


def quick_sort(sort):
    start = time.time()
    sort = quick(sort)
    end = time.time()
    operation_time = end - start
    print("quick sort time =     ", round(operation_time, 5))
    return sort


max_rand = 5000
number_of_number = 5000

list_to_sort1 = [random.randint(0, max_rand) for _ in range(number_of_number)]
list_to_sort2 = list_to_sort1[:]
list_to_sort3 = list_to_sort1[:]

list_to_sort1 = bubble_sort(list_to_sort1)
list_to_sort2 = selection_sort(list_to_sort2)
list_to_sort3 = quick_sort(list_to_sort3)
