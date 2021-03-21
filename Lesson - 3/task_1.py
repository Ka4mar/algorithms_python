"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание:  вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""

# работа со списком выполняется быстрее чем со словорем потому, что
# у словарей дополнительно затрачено время на вычисление хешей

import time


listing = []


def filling_li(li):

    start = time.time()
    for i in range(0, 100000):
        li.append(i)

    end = time.time()
    return listing, print(end - start)


filling_li(listing)


def sum_time_append(x):
    start = time.time()
    for i in range(x):
        listing.append(2)
    end = time.time()
    return end - start


print(sum_time_append(100000))


def sum_time_len(x):
    start = time.time()
    for i in range(x):
        len(listing)
    end = time.time()
    return end - start


print(sum_time_len(100000))


########################################################################################################################

diction = {}


def filling_dict(dic):

    start = time.time()
    for i in range(0, 100000):
        dic[i] = i
    end = time.time()
    return diction, print(end - start)


filling_dict(diction)


def sum_time_up(x):
    start = time.time()
    for i in range(x):
        diction.update({25: 25})
    end = time.time()
    return end - start


print(sum_time_up(100000))


def sum_time_len2(x):
    start = time.time()
    for i in range(x):
        len(diction)
    end = time.time()
    return end - start


print(sum_time_len2(100000))

