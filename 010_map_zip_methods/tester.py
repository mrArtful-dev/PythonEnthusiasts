# people = ['Jack Smith', 'Bob Brown', 'Sarah Gold', 'Vova Pupkin'];

# new_people = []
# for person in people:
#     if len(person) <= 10:
#         new_people.append(person)
#
# print(new_people)


# def name_filter(person):
#     if person[0] in 'JB':
#         return True
#     return False
#
#
# new_people = filter(lambda person: len(person) <= 10, people)
# print(list(new_people))
#
# new_people = filter(name_filter, people)
# print(list(new_people))

# people = [
#     {
#         'name': 'Jack',
#         'surname': 'Smith',
#         'has_children': True
#     },
#     {
#         'name': 'Sarah',
#         'surname': 'Smith',
#         'has_children': True
#     },
#     {
#         'name': 'Bob',
#         'surname': 'Gold',
#         'has_children': False
#     }
# ]
#
# parents = filter(lambda person: person['has_children'], people)
# print(list(parents))

# numbers = [1, 2, 54, 231, 213, 64, 233, 122, 56]
# evens = filter(lambda num: not num % 2, numbers)
# print(list(evens))

# people = [
#     {
#         'name': 'Jack',
#         'surname': 'Smith',
#         'has_children': True
#     },
#     {
#         'name': 'Sarah',
#         'surname': 'Smith',
#         'has_children': True
#     },
#     {
#         'name': 'Bob',
#         'surname': 'Gold',
#         'has_children': False
#     }
# ]
#
# new_people = map(lambda person: {
#                                     'fullname': f'{person["name"]} {person["surname"]}',
#                                     'children': person['has_children']
#                                 }, people)
# print(list(new_people))
# employee = [
#     {'Name':'Sravan','Salary':48000,'age':23},
#     {'Name':'Raghu','Salary':25000,'age':21},
#     {'Name':'Ram','Salary':21000,'age':12},
#     {'Name':'Shivani','Salary':148000,'age':14},
#     {'Name':'Salma','Salary':41000,'age':22}]
#
# new_employee = map(lambda emp: {'name': emp['Name'], 'info': {'salary': emp['Salary'], 'age': emp['age'], 'year_of_birth': 2023 - emp['age']}}, employee)
# print(list(new_employee))
# new_employee = map(lambda emp: [emp['Name'], emp['age']], employee)
# print(list(new_employee))
#
# adults = filter(lambda emp: emp['age'] >= 18 and not emp['Salary'] > 40000, employee)
# print(list(adults))

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# squares = map(lambda x: x ** 2, nums)
# print(list(squares))
#
# nums = [100, 200, 300, 400, 500]
# days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#
# large_list = zip(range(10), nums, days)
# print(list(large_list))
#
# test = enumerate(days, 10)
# print(list(test))
