"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

# Судя по замерам времени он иногда даже проигрывает вплане скорости выполнения , на  мой взгляд нет смысла
# его использовать в нынешнее время словарей с имеющейся хеш таблицей 

import collections
from timeit import timeit

new_dict = {1: 1, 2: 2, 3: 3}

new_order_dict = collections.OrderedDict([(1, 1), (2, 2), (3, 3)])

addition_dict = new_dict[4] = 4
print(timeit("addition_dict", globals=globals()))

addition_order = new_order_dict[4] = 4
print(timeit("addition_order", globals=globals()))

item_dict = new_dict.items()
print(timeit("item_dict", globals=globals()))

item_order = new_order_dict.items()
print(timeit("item_order", globals=globals()))


def search_dict():
    i = 0
    for key, value in new_dict.items():
       i += key


print(timeit("search_dict", globals=globals()))


def search_order():
    i = 0
    for key, value in new_dict.items():
       i += key


print(timeit("search_order", globals=globals()))


# 0.024860506999999997
# 0.026029811000000007
# 0.023662781999999993
# 0.027911261000000007
# 0.023382320999999984
# 0.02838289599999999
