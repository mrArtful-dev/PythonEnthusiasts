nums = [1, 2, 3, 4, 5]
squares = []

# for num in nums:
#     print(num ** 2)
#

# for num in nums:
#     squares.append(num ** 2)
#
# print(squares)

# for num in range(1, 101):
#     print(num ** 3)


people = [('Jack', 'Smith', 30), ('Mary', 'Gold', 19), ('Bob', 'Green', 15)]

# for person in people:
#     print(f'Hello {person[0]} {person[1]}. You are {person[2]} years old.')

# for name, surname, age in people:
#     print(f'Hello {name} {surname}. You are {age} years old.')

# for name, surname, age in people:
#     if age >= 18:
#         print(f'Hello {name} {surname}. You are {age} years old. You are adult!')
#     else:
#         print(f'Hello {name} {surname}. You are {age} years old. You are a child!')

for num1 in range(10):
    for num2 in range(10):
        for num3 in range(10):
            for num4 in range(10):
                print(num1, num2, num3, num4)
