"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.

Пример:
Введите номер буквы: 4
Введёному номеру соответствует буква: d

Подсказка: используйте ф-ции chr() и ord()
"""

try:
    NUMB = int(input("Введите номер буквы: "))
    print(f"Введёному номеру соответствует буква: {chr(ord('a') + NUMB - 1)}")
except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь")
