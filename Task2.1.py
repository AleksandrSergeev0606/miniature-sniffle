from calendar import monthrange

print("Введите год")
a = int(input())
print("Введите номер месяца от 1 до 12")
b = int(input())
days = monthrange(a, b) [1]
if b == 1:
    print("В январе ", a, " года", days, " дней")
elif b == 2:
    print("В феврале ", a, " года", days, " дней")
elif b == 3:
    print("В марте ", a, " года", days, " дней")
elif b == 4:
    print("В апреле ", a, " года", days, " дней")
elif b == 5:
    print("В мае ", a, " года", days, " дней")
elif b == 6:
    print("В июне ", a, " года", days, " дней")
elif b == 7:
    print("В июле ", a, " года", days, " дней")
elif b == 8:
    print("В августе ", a, " года", days, " дней")
elif b == 9:
    print("В сентябре ", a, " года", days, " дней")
elif b == 10:
    print("В октябре ", a, " года", days, " дней")
elif b == 11:
    print("В ноябре ", a, " года", days, " дней")
elif b == 12:
    print("В декабре ", a, " года", days, " дней")