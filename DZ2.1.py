print("Введите список чисел:")
a = input().split()
l = []
for i in range(len(a)):
    l.append(int(a[i]))
print(l)

x = 0
y = 0
z = 0
for i in range(len(l)):
    for ii in range(len(l)):
        if l[i] / l[ii] == 1:
            x = x+1
    if x < 2:
        y = l[i]
        z = z + 1
    else:
        x = 0
if z < 1:
    print("В строке все числа повторяются")
else:
    print("В списке не повторяется число:", y)