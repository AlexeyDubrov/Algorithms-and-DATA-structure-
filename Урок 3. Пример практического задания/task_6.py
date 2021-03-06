"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа

Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6)  и максимальным (88) элементами: 234
"""

from random import randint


def task_6(lst):
    """Задача 6"""

    print(f"Массив: {lst}")

    min_index = 0
    max_index = 0
    step = 1
    common_sum = 0

    for i in lst:
        if lst[min_index] > i:
            min_index = lst.index(i)
        elif lst[max_index] < i:
            max_index = lst.index(i)

    if max_index - min_index < 0:
        step = -1

    for i in lst[min_index + step:max_index:step]:
        common_sum += i

    print(
        f"Сумма элементов между минимальным ({lst[min_index]})",
        f" и максимальным ({lst[max_index]}) элементами: {common_sum}"
    )


try:
    NUM = int(input('Введите количество элементов в массиве: '))
    LST = [randint(1, 100) for x in range(NUM)]
    task_6(LST)
except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь")
