from datetime import datetime, timedelta

# Под каждым комментарием нужно написать одну функцию/программу
# Задание в комментарии
# input - параметр который функция получает
# output - параметр который функция возвращает



# # Write a program that converts given string to datetime object
sample1 = 'Jan 1 2014 2:43PM'
sample2 = '14:20 10/12/22'  # YY/MM/DD
sample3 = 'Tuesday, September 24, 2019'
sample4 = '01.01.1970 - 00:00:01'

result1 = datetime.strptime(sample1, '%b %d %Y %I:%M%p')
print(result1)
result2 = datetime.strptime(sample2, '%H:%M %y/%m/%d')
print(result2)
result3 = datetime.strptime(sample3, '%A, %B %d, %Y')
print(result3)
result4 = datetime.strptime(sample4, '%d.%m.%Y - %H:%M:%S')
print(result4)

# Write a program to print yesterdays, today and tomorrow dates

# current_date = datetime.now().date()
# yesterday_date = current_date - timedelta(days=1)
# tomorrow_date = current_date + timedelta(days=1)
#
# print("Today:", current_date)
# print("Yesterday:", yesterday_date)
# print("Tomorrow:", tomorrow_date)


# Write a program to convert given timestamp to dd.mm.yyyy format
some_day = 1014163200
timestamp = strftime(some_day)
new_date = timestamp.strftime("%d.%b.%Y")
print(new_date)

# Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)