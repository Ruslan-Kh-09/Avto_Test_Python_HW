import math


def s_square(side):

    if not float(side).is_integer():
        return math.ceil(side * side)
    return side * side


num_side = float(input("Введите длину стороны квадрата: "))
print(f"Площадь вашего квадрата = {s_square(num_side)}")
