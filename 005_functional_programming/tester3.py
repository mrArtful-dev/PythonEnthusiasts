# a = 50
# b = 100
# c = 150
#
#
# def sample():
#     global b, c
#     a = 5
#     b += 10
#     c += 100
#     print(a, b, c)
#
#
# print(a, b, c)
# sample()
# sample()
# sample()
# sample()
# sample()

def sample2(a, b, c=1, *args, **kwargs):
    print(a * b * c)
    for arg in args:
        print(arg)
    print(kwargs)


sample2(12, 12, 3, 'hello', 1, 'asdasd', 123, 0.32, [1, 2, 3], name='Jack', x=10, surname='Smith')