import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
numbers2 = [4, 5, 4, 3, 2, 1, 0, 4, 6, 98]
selectors = [True, False, False, True]

# result = itertools.compress(letters, selectors)
# print(list(result))

# result = itertools.filterfalse(lambda x: x > 2, numbers2)
# print(list(result))

# result = itertools.dropwhile(lambda x: x > 2, numbers2)
# print(list(result))
#
# result = itertools.takewhile(lambda x: x > 2, numbers2)
# print(list(result))

result = itertools.accumulate(numbers2)
print(list(result))

result = sum(numbers2)
print(result)
