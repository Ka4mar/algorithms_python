
import hashlib

"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

url_list = {}


def url(x):

    salt = "022cf2d005a201ab60"
    new_url = hashlib.sha256(salt.encode() + x.encode()).hexdigest()
    if new_url in url_list:
        print("Такая уже страница есть")
    else:
        url_list[new_url] = x

    return print(url_list)


url("http")
