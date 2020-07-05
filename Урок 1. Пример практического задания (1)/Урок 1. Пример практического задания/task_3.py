"""
Задание 3. По введенным пользователем координатам двух
точек вывести уравнение прямой,
проходящей через эти точки.

Подсказка:
Запросите у пользователя значения координат X и Y для первой и второй точки
Найдите в учебнике по высшей математике формулы расчета:
k – угловой коэффициент (действительное число), b – свободный член (действительное число)
Сформируйте уравнение прямой по формуле: y = kx + b – функция общего вида

Пример:
X1_VAL = 2, Y1_VAL = 3, X2_VAL = 4, Y2_VAL = 5
Уравнение прямой, проходящей через эти точки: y = 1.0x + 1.0
"""

try:
    X1_VAL = int(input('Введите координату X точки 1: '))
    Y1_VAL = int(input('Введите координату Y точки 1: '))
    X2_VAL = int(input('Введите координату X точки 2: '))
    Y2_VAL = int(input('Введите координату Y точки 2: '))

    try:
        K_PARAM = (Y2_VAL - Y1_VAL) / (X2_VAL - X1_VAL)
        B_PARAM = Y2_VAL - K_PARAM * X2_VAL
        print(f"Уравнение прямой, проходящей через эти точки: y = {K_PARAM}x + {B_PARAM}")
    except ZeroDivisionError:
        print("Ой, кажется мы пытаемся делить на 0. Проверьте корректность координат")

except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь")
