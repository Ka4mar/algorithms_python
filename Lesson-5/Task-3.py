"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям
И добавить аналитику, так ли это или нет.!
"""

# Итог: вслучае использования встроенных функций deque по скорости будет быстрее, однако при случае где нужен
# непосредственно доступ к элементу по скорости он проигрывает


from timeit import timeit
from collections import deque


one = list("ssd")
two = list("zxc")

deq_one = deque(one)

deq_app = deq_one.appendleft("s")
print(timeit("deq_app", globals=globals()))

list_app = two.insert(0, "d")
print(timeit("list_app", globals=globals()))

deq_pop = deq_one.popleft()
print(timeit("deq_pop", globals=globals()))

list_pop = two.pop()
print(timeit("list_pop", globals=globals()))


def deq(x):
    for i in x:
        i += i


print(timeit("deq(deq_one)", globals=globals(),))


def li(y):
    for i in y:
        i += i


print(timeit("li(two)", globals=globals()))


# 0.030690670000000003
# 0.025808605
# 0.034939417000000014
# 0.025737818999999995
# 0.409890953
# 0.42161804199999997
