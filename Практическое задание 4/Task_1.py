"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры
Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""

# list comprehension будет быстрее потому что нету дополнительных использований встроенных функций,
# в нашем случае append, выполнение функции будет быстрее но не сказать , что прямо значительно


from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


numbers = [elem for elem in range(1000)]

print(
    timeit(
        "func_1(numbers)",
        globals=globals(),
        number=1000))


print(
    timeit(
        "func_2(numbers)",
        globals=globals(),
        number=1000))


numbers_2 = [elem for elem in range(10000)]

print(
    timeit(
        "func_1(numbers_2)",
        globals=globals(),
        number=1000))


print(
    timeit(
        "func_2(numbers_2)",
        globals=globals(),
        number=1000))


numbers_3 = [elem for elem in range(100000)]

print(
    timeit(
        "func_1(numbers_3)",
        globals=globals(),
        number=1000))


print(
    timeit(
        "func_2(numbers_3)",
        globals=globals(),
        number=1000))