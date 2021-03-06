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
Введите первое шеснадцатиричное число: A2
Введите второе шеснадцатиричное число: C4F
Сумма чисел = ['c', 'f', '1']
Произведение чисел = ['7', 'c', '9', 'f', 'e']
"""

class HexOperation:
    def __init__(self, num_first, num_second):
        self.num_first = num_first
        self.num_second = num_second

    def __add__(self, other):
        return list(hex(int(''.join(self.num_first), 16) + int(''.join(other.num_second), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.num_first), 16) * int(''.join(other.num_second), 16)))[2:]


hex_num_first = list(input('Введите первое шеснадцатиричное число: '))
hex_num_second = list(input('Введите второе шеснадцатиричное число: '))

res_sum = HexOperation(hex_num_first, hex_num_second) + HexOperation(hex_num_first, hex_num_second)
res_mul = HexOperation(hex_num_first, hex_num_second) * HexOperation(hex_num_first, hex_num_second)
print(f'Сумма чисел = {res_sum}\nПроизведение чисел = {res_mul}')
