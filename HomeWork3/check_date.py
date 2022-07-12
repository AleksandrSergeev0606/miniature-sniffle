def check_date(day, month, year):
    if day > 31 or day < 1 or ((month == 4 or month == 6 or month == 9 or month == 11) and day > 30) or (
            (year % 400 == 0 or year % 4 == 0) and month == 2 and day > 29) or (
            year % 100 == 0 and month == 2 and day > 28) or (month == 2 and day > 28):
        print("FAILED")
        print("incorrect day")
        if month > 12 or month < 1:
            print("FAILED")
            print("incorrect month")
    else:
        print("OK")
