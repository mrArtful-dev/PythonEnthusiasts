# counter = -100
#
# while 0 < counter <= 100:
#     print(counter)
#     counter -= 1


# current_position = 0
# distance_to_target = 1000
#
# step = 0.54
# total_steps = 0
#
# while current_position < distance_to_target:
#     current_position += step
#     total_steps += 1
#
# print(total_steps)

# counter = 0
# while True:
#
#     if counter > 100:
#         break
#
#     counter += 1
#     if counter == 95:
#         continue
#     print(counter)


# # ValueError
# int('asdasdasddasdas')

try:
    int('13212321')
    5 / 0
except ValueError:
    print('Cannot convert to int!')
except ZeroDivisionError:
    print('Cannot divide by 0')
else:
    print('All is good!')
finally:
    print('I am finished!')

print('I am still running!')