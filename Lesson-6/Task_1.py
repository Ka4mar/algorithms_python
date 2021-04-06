"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.
Можно взять задачи с курса Основ
или с текущего курса Алгоритмов
Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
import json
from pympler import asizeof
from collections import namedtuple
import memory_profiler
# GENERATOR #######################################################################################################


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


@decor
def generator(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num * num


def search_min_value():

    arr, mem_diff = generator(list(range(100000))) # GeneraTor
    min_value = None

    for i in arr:
        bull = 1
        for a in arr:
            if i > a:
                bull = 0
                break
        if bull == 1:
            min_value = i
            break
    print(f"{mem_diff}")
    return min_value


print(search_min_value())


# С реализация заключается в использованием генератораб, который не требует памяти для хранения данных в нём
# потому что получаем данные по запросу получилось 0.00390625 Mib
# изначально использовался итератор для создания массива и получилось 1.9375 Mib Разница больше в 400 раз в обьеме
# используемой памяти

i = 1
quantity_company = int(input("Введите количество компаний для посчета прибыли: "))

companies = namedtuple("Company", "name, quarter_1, quarter_2, quarter_3, quarter_4")
save = {}


def profit_count(num):
    i = 1
    list_comp = {}
    below_average = []
    above_average = []

    while i <= num:
        i += 1
        sum_comp = 0
        name = ""
        comp = (companies(name="e", quarter_1=2,
                          quarter_2=2,
                          quarter_3=2,
                          quarter_4=2))
        save[comp] = i+1
        for x in comp:
            if type(x) == str:
                name = x
            else:
                sum_comp += x

        list_comp[name] = sum_comp

    average_amount = sum(list_comp.values()) / (i-1)
    print(f"Средняя годовая прибыль: {average_amount}")

    for key, value in list_comp.items():
        if average_amount > value:
            above_average.append(key)
        else:
            below_average.append(key)


dumped_dict = json.dumps(save)
profit_count(quantity_company)

print(asizeof.asizeof(save))
print('Размер json: ', asizeof.asizeof(dumped_dict))


# Перивел словари типа namedtuple в формат json чем
# в формате namedtuple 432 байт получилось по замером,
# а в Размер json:  56. Следовательно получилось создать реализыцию для экономии памяти при хранение файла с данными


my_list = map(str, range(100000))

print(my_list)


def check_event_1(lst):
    new_list = [int(i) for i in lst]
    return new_list


@decor
def yes(arg):
    new = []

    for x in arg:
        if x % 2 == 0:
            new.append(x)
    print(asizeof.asizeof(map(str, new)))
    print(asizeof.asizeof(new))


res, mem_diff = yes(check_event_1(list(range(1000000))))
print(f"Выполнение заняло {mem_diff} Mib")

# Проверка реализации и улучщения были в хранение окончательного файла с вариантом в массиве или в формате map
# получилось в формате мар  в размере 48 байт, а в изначальном массиве вышло 20290000 байт
