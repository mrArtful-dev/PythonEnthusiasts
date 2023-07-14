import datetime
"""
Под каждым комментарием нужно написать одну функцию/программу
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""


# 1- Write a program that converts given string to datetime object
sample1 = 'Jan 1 2014 2:43PM'
sample2 = '14:20 10/12/22'  # YY/MM/DD
sample3 = 'Tuesday, September 24, 2019'
sample4 = '01.01.1970 - 00:00:01'

from datetime import datetime

# Sample 1: Jan 1 2014 2:43PM
sample1_format = '%b %d %Y %I:%M%p'
sample1_datetime = datetime.strptime(sample1, sample1_format)
print("Sample 1:", sample1_datetime)

# Sample 2: 14:20 10/12/22
sample2_format = '%H:%M %d/%m/%y'
sample2_datetime = datetime.strptime(sample2, sample2_format)
print("Sample 2:", sample2_datetime)

# Sample 3: Tuesday, September 24, 2019
sample3_format = '%A, %B %d, %Y'
sample3_datetime = datetime.strptime(sample3, sample3_format)
print("Sample 3:", sample3_datetime)

# Sample 4: 01.01.1970 - 00:00:01
sample4_format = '%m.%d.%Y - %H:%M:%S'
sample4_datetime = datetime.strptime(sample4, sample4_format)
print("Sample 4:", sample4_datetime)


# 2- Write a program to print yesterdays, today and tomorrow dates
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print("Yesterday's date:", yesterday)
print("Today's date:", today)
print("Tomorrow's date:", tomorrow)


# 3- Write a program to convert given timestamp to dd.mm.yyyy format
some_day = 1014163200

from datetime import datetime

# Given timestamp
timestamp = 1014163200

# Convert timestamp to datetime object
dt_object = datetime.fromtimestamp(timestamp)

# Format datetime object as dd.mm.yyyy
formatted_date = dt_object.strftime('%d.%m.%Y')

# Print the formatted date
print("Formatted date:", formatted_date)


# 4- Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)

import datetime

def subtract_two_weeks(timestamp):
    # Convert timestamp to datetime object
    dt_object = datetime.datetime.fromtimestamp(timestamp)

    # Subtract two weeks from the datetime object
    new_dt_object = dt_object - datetime.timedelta(weeks=2)

    # Convert the new datetime object back to a timestamp
    new_timestamp = new_dt_object.timestamp()

    return new_timestamp

timestamp = 1631433600.0  # Example timestamp
new_timestamp = subtract_two_weeks(timestamp)
print("New timestamp:", new_timestamp)