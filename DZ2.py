print("Введите список чисел:")
a = input().split()
l = []
for i in range(len(a)):
    l.append(int(a[i]))
print(l)

max = l[0]
for i in range(len(l)):
    if l[i] > max:
      max = l[i]
print("Максимальное число из списка: ", max)

min = l[0]
for i in range(len(l)):
    if l[i] < min:
      min = l[i]
print("Минимальное число из списка: ", min)

n = []
m = []
for i in range(len(l)):
    if l[i] % 3 == 0 and l[i] % 5 != 0:
      n.append(l[i])
for i in n:
    if i not in m:
        m.append(i)
print("Числа, которые делятся на 3, но не делятся на 5: ", m)