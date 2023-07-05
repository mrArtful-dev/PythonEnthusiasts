id_code = input('Please enter your ID code: ')
def check_id(id_code):
    def count_check_number(id_code, chk_list):
        result = 0
        counter = 0
        for num in chk_list:
            result = result + num * int(id_code[counter])
            counter += 1
        return result % 11

    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    if int(id_code[10]) == count_check_number(id_code, chk1):
        return print('ID code is valid')
    elif count_check_number(id_code, chk1) == 10:
        if int(id_code[10]) == count_check_number(id_code, chk2):
            return print('ID code is valid')
        elif count_check_number(id_code, chk2) == 10 or count_check_number(id_code, chk2) == 0:
            if int(id_code[10] == 0):
                return print('ID code is valid')
            else:
                return print('ID code is invalid')
        else:
            return print('ID code is not valid')
    else:
        return print('ID code is not valid')

check_id(id_code)