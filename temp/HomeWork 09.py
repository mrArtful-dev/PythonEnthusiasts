import re

 # 1. Напишите регулярное выражение для поиска HTML-цвета, заданного как #ABCDEF, то есть # и содержит затем 6 шестнадцатеричных символов.
	# HASH цвета используют значения от 0 до 15, где 0-9 цифры от 0 до 9, 10-15 буквы от A-F.


html = ''' #ABCDEF and #123456, #564acd - #5c6a55 '''
pattern = re.compile(r'#([0-9a-fA-F]{6})')
natches = re.findall(pattern, html)
print(natches)
#
# for natch in natches:
#     print(natch)

# 2. Создать запрос для определения в тексте цифр, за которыми не стоит знак +. (Примеры выражений “2*9-6*5” или (3+5)-9*4)

primer = ''' “2*9-6*5” или (3+5)-9*4) 54156811'''
pattern2 = re.compile(r'\d(?!\+)')
natches2 = re.findall(pattern2, primer)
print(natches2)

#
# # 3. Найти в тексте время. Время имеет формат часы:минуты.
# #     И часы, и минуты состоят из двух цифр, пример: 09:00.
# #     Напишите регулярное выражение для поиска времени в строке:
# #     «Завтрак в 09:00». Учтите, что «37:98» – некорректное время.
# #     00:00 - 23:59 (234:23, 23:243, 123:213 не является временем)
#
# timeses = '''  00:00 - 23:59 (234:23, 23:243, 123:213 09:03 «37:98» 23:67'''
#
# pattern3 = re.compile(r'\b[0-2][0-9]:[0-5]\d\b')
# natches3 = re.findall(pattern3, timeses)
# for natch3 in natches3:
#     print(natch3)
#
# # 4. Написать программу котороая будет выбирать из файла people.txt:
# # 	1) Все имена и фамилии
# # 	2) Все адреса
#
with open('../009_regular_exp/people.txt', 'r', encoding='utf8') as txt_file:
    txt_content = txt_file.read()
    pattern_name = re.compile(r'([A-Z]\w+\b \b[A-Z][\w-]+)$', re.MULTILINE)
    natches_name = re.findall(pattern_name, txt_content)
    print(len(natches_name))
    for natch_name in natches_name:
        print(natch_name)
    pattern_addres = re.compile(r'\b\d{3} \D+ \d{5}\b')
    natches_addres = re.findall(pattern_addres, txt_content)
    print(len(natches_addres))
    for natch_addres in natches_addres:
        print(natch_addres)

#
# 5. Написать регулярное выражение для проверки строки,
#   задача определить состоит ли строка из символов a-z, A-Z, 0-9.


text = re.compile(r'^[a-zA-Z0-9]+$')


# if text True
#     print('ok')
# else
#     print('no ok')
#
#


# 6. Написать регулярное выражение для определения эстонского личного кода (isikukood)
#
# Все строки произвольные.

id = str(38512310280) #385 12 31
# id = str(id)

pattern_id = re.compile(r'[1-8]\d{2}([01-9]|[11-9])')
natches_id = re.findall(pattern_id, id)

print(natches_id)