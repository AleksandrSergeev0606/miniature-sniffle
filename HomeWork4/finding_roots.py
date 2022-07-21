import math


def roots(A, B, C):
    D = B * B - 4 * A * C
    if D > 0:
        x1 = - ((B + math.sqrt(D)) / (2 * A))
        x2 = - ((B - math.sqrt(D)) / (2 * A))
        print("Корни квадратного уравнения:", x1, ",", x2)
    if D == 0:
        x = - (B / (2 * A))
        print("Корень квадратного уравнения:", x)
    if D < 0:
        print("Нет корней")
    return A, B, C
