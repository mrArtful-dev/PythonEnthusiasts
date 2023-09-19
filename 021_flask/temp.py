import hashlib

password = hashlib.md5('hello124'.encode()).hexdigest()

print(password)
#
# if hashlib.md5(input('Enter pass: ').encode()).hexdigest() == password:
#     print('OK')
# else:
#     print('NOK')

# 74d8ca4c9edab62f2901344d86753d3f