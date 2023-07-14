
from datetime import datetime, timedelta

"""
Под каждым комментарием нужно написать одну функцию/программу
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""



# Write a program that converts given string to datetime object
sample1 = 'Jan 1 2014 2:43PM'
sample2 = '14:20 10/12/22'  # YY/MM/DD
sample3 = 'Tuesday, September 24, 2019'
sample4 = '01.01.1970 - 00:00:01'

new_dt1 = datetime.strptime(sample1, '%b %d %Y %I:%M%p')
print(new_dt1)
new_dt2 = datetime.strptime(sample2, '%H:%M %y/%m/%d')
print(new_dt2)
new_dt3 = datetime.strptime(sample3, '%A, %B %d, %Y')
print(new_dt3)
new_dt4 = datetime.strptime(sample4, '%d.%m.%Y - %H:%M:%S')
print(new_dt4)


# Write a program to print yesterdays, today and tomorrow dates
# from datetime import date

current_date = datetime.today()
yesterdays = datetime.today() - timedelta(hours=24)
tomorow = datetime.today() + timedelta(days=1)
print(yesterdays)
print(current_date)
print(tomorow)


# Write a program to convert given timestamp to dd.mm.yyyy format

some_day = 1014163200
s_d = datetime.fromtimestamp(some_day)
s_dstring = s_d.strftime("%d.%b.%Y")
print(s_dstring)



# Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)

date_today =float(input('Za Imput6 Float 00.00 '))
date_2weks_off = datetime.fromtimestamp(date_today) - timedelta(weeks=2)
print(datetime.timestamp(date_2weks_off))