"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.
Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""

mno = set()


def substrings(word):
    for beg in range(len(word)):
        for end in range(beg, len(word)):
            if word[beg:end + 1] != word:
                mno.add(hash((word[beg:end + 1])))
    return print(word)


substrings("papa")
print(mno)

