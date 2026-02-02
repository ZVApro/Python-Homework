import math
def square(a):
    return math.ceil(a*a)
a = float(input('Введите значение стороны: '))
print(f'Площадь равна: {square(a)}')