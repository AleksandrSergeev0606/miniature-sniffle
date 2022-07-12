from check_date import check_date

print("Введите дату в формате 'ДД.ММ.ГГГГ'")
date_in = input()
date = date_in.split('.')
day = int(date[0])
month = int(date[1])
year = int(date[2])
result = check_date(day, month, year)
