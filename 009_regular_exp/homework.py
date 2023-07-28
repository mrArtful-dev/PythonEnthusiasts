import re

# pattern1 = re.compile(r'#[0-9a-fA-F]{6}')
#
# matches = pattern1.finditer('#123123 #KK2312 #123add #KLERAA')
#
# for match in matches:
#     print(match)
#

# pattern2 = re.compile(r'\b\d+(?![+\d])')
#
# matches = pattern2.finditer('2*9-6*5” или (3+5)-9*4) 213221+ 213123')
#
# for match in matches:
#     print(match)


# pattern3 = re.compile(r'\b([01][0-9]|2[0-3]):[0-5]\d\b')
#
# matches = pattern3.finditer('«37:98» – некорректное время. 00:00 - 23:59 (234:23, 23:243, 123:213 не является временем)')
#
# for match in matches:
#     print(match)




# with open('../009_regular_exp/people.txt', 'r', encoding='utf8') as file:
#     data = file.read()
#
# name_pattern = re.compile(r'([A-Za-z-]+ [A-Za-z-]+)\n')
# address_pattern = re.compile(r'\d{3} [0-9A-Za-z\'-]+ St., [A-Za-z\' -]+ [A-Z]{2} \d{5}')
#
# names = name_pattern.finditer(data)
# # print(len(list(names)))
# for match in names:
#     print(match.group(1))
#
# addresses = list(address_pattern.finditer(data))
# for match in addresses:
#     print(match)
#
# print(len(addresses))


# pattern4 = re.compile(r'^[a-zA-Z0-9]+$')
#
# pattern4 = re.compile(r'[^a-zA-Z0-9]')
#
# matches = pattern4.findall('123asdasdASDAS')
# print(matches)
#
# if len(matches):
#     print('BAD')
# else:
#     print('GOOD')


pattern5 = re.compile(r'[1-8]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])\d{4}')

matches = pattern5.finditer('38803160272 98802144578 45615221234 45612482131')

for match in matches:
    print(match)