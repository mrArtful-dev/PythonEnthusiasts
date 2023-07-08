print('027' > '010')


isikukood = '38803160081'

print(isikukood[7:10] <= '010')

id_tuple = []
for letter in isikukood:
    id_tuple.append(int(letter))

print(id_tuple)
