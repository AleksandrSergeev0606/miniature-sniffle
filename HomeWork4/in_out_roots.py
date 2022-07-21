from finding_roots import roots
import matplotlib.pyplot as plt
import numpy as np

p = 0
while p == 0:
    print("Введите коэффициенты A, B и C квадратного уравнения Ax^2 + Bx + C = 0")
    coef = input()
    separate = coef.split(' ')
    A = int(separate[0])
    B = int(separate[1])
    C = int(separate[2])
    p = 1
    if A == 0:
        print("Это линейное уравнение! Коэффициент А не должен быть равен нулю. Введите коэффициенты заново.")
        p = 0
result = roots(A, B, C)


x = np.linspace(-5, 5, 100)
y = A * x * x + B * x + C
plt.title('Зависимость y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.plot(x, y)
plt.show()
