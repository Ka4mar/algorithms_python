"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1
Предприятия, с прибылью ниже среднего значения: Фирма_2
"""

from collections import namedtuple

quantity_company = int(input("Введите количество компаний для посчета прибыли: "))

companies = namedtuple("Company", "name, quarter_1, quarter_2, quarter_3, quarter_4")


def profit_count(num):
    i = 1
    list_comp = {}
    below_average = []
    above_average = []

    while i <= num:
        i += 1
        sum_comp = 0
        name = ""
        comp = (companies(name=input("Введите название компании: "), quarter_1=int(input("Прибыль за 1 квартал: ")),
                          quarter_2=int(input("Прибыль за 2 квартал: ")),
                          quarter_3=int(input("Прибыль за 3 квартал: ")),
                          quarter_4=int(input("Прибыль за 4 квартал: "))))

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

    print(f"Предприятия, с прибылью выше среднего значения: {''.join(above_average)}")
    print(f"Предприятия, с прибылью ниже среднего значения: {''.join(below_average)}")


profit_count(quantity_company)