print("Введите список чисел:")
a = input().split()
l = []
for i in range(len(a)):
    l.append(int(a[i]))
print(l)
n = []
m = []
for i in range(len(l)):
    n.append(l[i])
for i in n:
    if i not in m:
        m.append(i)
print(len(m))
