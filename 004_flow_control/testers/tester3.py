condition = True
while condition:
    user_choice = input('Please choose:\n1. Check ID\n0. Exit\n--> ')

    # IF statement for user to choose option
    if user_choice == '1':

        condition2 = True
        while condition2:
            try:
                user_id = input('Please enter your Estonian national ID: ')
                user_id = str(int(user_id))
                if len(user_id) != 11:
                    if len(user_id) > 11:
                        print('Code you entered is longer than 11 digits')
                        raise UserWarning
                    elif len(user_id) < 11:
                        print('Code you entered is shorter than 11 digits')
                        raise UserWarning
            except ValueError:
                print('Text you enetered is not numeric!')
                print('Please try again')
            except:
                print('Please try again!')
            else:
                gender_id = user_id[0]
                birth_year = user_id[1:3]
                birth_month = user_id[3:5]
                birth_day = user_id[5:7]
                birth_region = int(user_id[7:10])
                chech_num = user_id[10]

                # Gender control
                if int(gender_id) % 2 == 0:
                    gender = 'Female'
                else:
                    gender = 'Male'

                # Century control
                if gender_id == '1' or gender_id == '2':
                    birth_cent = '18'
                elif gender_id == '3' or gender_id == '4':
                    birth_cent = '19'
                elif gender_id == '5' or gender_id == '6':
                    birth_cent = '20'

                # Region control
                if birth_region in range(1, 11):
                    region = 'Kuressaare haigla'
                elif birth_region in range(11, 20):
                    region = 'Tartu Ülikooli Naistekliinik'
                elif birth_region in range(21, 151):
                    region = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
                else:
                    region = 'unknown region'

                print('Your national id is: ' + user_id)
                print('You are ' + gender)
                print('Your date of birth is ' + birth_day + '.' + birth_month + '.' + birth_cent + birth_year)
                print('You were born in ' + region)
                condition2 = False


    elif user_choice == '0':
        print('Good bye!')
        quit()
    else:
        print('Choice is out of range.')
