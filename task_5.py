"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""


class Class:
    def __init__(self, max_quantity):
        self.elem = [[]]
        self.max_quantity = max_quantity

    def __str__(self):
        return str(self.elem)

    def push_in(self, el):
        if len(self.elem[len(self.elem)-1]) < self.max_quantity:
            self.elem[len(self.elem)-1].append(el)
        else:
            self.elem.append([])
            self.elem[len(self.elem)-1].append(el)

    def quantity_plates(self):
        sum_plates = 0
        for pile in self.elem:
            sum_plates += len(pile)
        return sum_plates

    def pile_count(self):
        return len(self.elem)


pla = Class(3)
pla.push_in(1)
pla.push_in(2)
pla.push_in(4)
pla.push_in(6)
pla.push_in(3)
pla.push_in(4)
pla.quantity_plates()
pla.pile_count()
print(pla.pile_count())
print(pla)
