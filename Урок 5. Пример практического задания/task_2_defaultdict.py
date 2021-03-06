"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

Пример:
Введите 1-е натуральное шестнадцатиричное число: A2
Введите 2-е натуральное шестнадцатиричное число: C4F
defaultdict(<class 'list'>, {'1-A2': ['A', '2'], '2-C4F': ['C', '4', 'F']})
Сумма:  ['C', 'F', '1']
Произведение:  ['7', 'C', '9', 'F', 'E']
"""

import collections
import functools


def calc():
    nums = collections.defaultdict(list)
    for d in range(2):
        n = input(f"Введите {d+1}-е натуральное шестнадцатиричное число: ")
        nums[f"{d+1}-{n}"] = list(n)
    print(nums)

    summ = sum([int(''.join(i), 16) for i in nums.values()])
    # '%X'	Число в шестнадцатеричной системе счисления (буквы в верхнем регистре)
    print("Сумма: ", list('%X' % summ))

    mult = functools.reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in nums.values()])
    print("Произведение: ", list('%X' % mult))


calc()
