"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.
Задачу можно решить без сортировки исходного
массива.
Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...
[5, 3, 4, 3, 3, 3, 3]
[3, 3, 3, 3, 3, 4, 5]
my_lst
new_lts
arr[m]
from statistics import median
[3, 4, 3, 3, 5, 3, 3]
left.clear()
right.clear()
m = 3
len = 7
i
left = []
right = []
left == right and
for i in
    for
    left == right
    left.clear()
    right.clear()
"""
import random

m = int(input("Введите число: "))

arr = [random.randint(0, 50) for _ in range(2*m+1)]

# 1
def gnome(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data


print(gnome(arr))
print(arr[m])

# 3


def note(x):
    for i in range(int(len(x)/2)):
        arr.remove(max(x))

    return max(x)


print(note(arr))