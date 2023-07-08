# def sum_two_numbers(num1, num2):
#     print(num1 + num2)
#
# x = 5
# y = 10
#
# sum_two_numbers('Hello', 'World')

# def say_hello():
#     print('Hello world!')
#     return 'Hello world'
#
#
# print(say_hello())

# def double(number):
#     return number * 2
#
#
# def triple(number):
#     return number * 3
#
#
# print(double(6) + triple(9))
#
# print(double(triple(7)) ** 0.5)

# def print_message(name, age, profession):
#     print(f'Hello {name}. You are {age} years old. You work as {profession}.')
#
#
# print_message('Jack', 25, 'plumber')
# print_message('Mary', 20, 'electrician')

# def print_message(person):
#     print(f'Hello {person[0]}. You are {person[1]} years old. You work as {person[2]}.')
#
#
# print_message(['Jack', 25, 'plumber'])

def area(width, height):
    return width * height


def perimeter(width, height):
    return (width + height) * 2


def material_amount(data):
    result_dict = {}
    for key, value in data.items():
        product_area = area(value[0], value[1])
        carpet_material = product_area * value[2] / 1000
        product_perimeter = perimeter(value[0], value[1])
        edge_material = product_perimeter * value[2] / 100
        result_dict[key] = {'carpet material': carpet_material, 'edge material': edge_material}

    return result_dict


def print_results(results):
    total_carpet_material = 0
    total_edge_material = 0
    for key, value in results.items():
        print(f'Carpet material for {key}: {value["carpet material"]}')
        print(f'Edge material for {key}: {value["edge material"]}')
        total_carpet_material += value['carpet material']
        total_edge_material += value['edge material']
    print()
    print(f'Total carpet material {total_carpet_material}')
    print(f'Total edge material {total_edge_material}')


order = {'small': [20, 20, 40], 'medium': [40, 60, 35], 'large': [50, 90, 22], 'x-large': [100, 120, 50], 'xx-large': [200, 200, 10]}
order2 = {'small': [20, 20, 40], 'medium': [40, 60, 35], 'large': [50, 90, 22], 'x-large': [100, 120, 50], 'xx-large': [200, 200, 10]}
order3 = {'small': [20, 20, 40], 'medium': [40, 60, 35], 'large': [50, 90, 22], 'x-large': [100, 120, 50], 'xx-large': [200, 200, 10]}

full_order = [order, order2, order3]


for x in full_order:
    print_results(material_amount(order))