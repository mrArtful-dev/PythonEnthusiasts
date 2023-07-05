def count_integers():
    counter = 0
    def counter_increment():
        return counter + 1
    return counter_increment()

print(count_integers())
print(count_integers())