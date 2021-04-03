"""
2.*	Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
__mul__
__add__
Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
1. вариант
defaultdict(list)
int(, 16)
reduce
2. вариант
class HexNumber:
    __add__
    __mul__
hx = HexNumber
hx + hx
"""

from collections import defaultdict

one_default = defaultdict(list)
one_default[1] = list((input("Введите первое число в шестнадцатиричной системе: ").upper()))
one_default[2] = list((input("Введите втрое число в шестнадцатиричной системе: ").upper()))


def sum_default(x):
    s = 0
    for key, value in x.items():
        if sum == 0:
            s = int((''.join(value)), 16)
        else:
            s += int((''.join(value)), 16)
    return print(f"Сумма чисел ровна: {list(hex(s)[2:].upper())}")


def work_default(x):
    s = 0
    for key, value in x.items():
        if s == 0:
            s = int((''.join(value)), 16)
        else:
            s = s * int((''.join(value)), 16)
    return print(f"Сумма чисел ровна: {list(hex(s)[2:].upper())}")


sum_default(one_default)
work_default(one_default)

