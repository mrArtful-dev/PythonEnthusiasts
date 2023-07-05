
while True:
    isikukood = input('Please enter ID or type "x" to exit: ')
    # isikukood = '38803160272'
    if isikukood.lower() == 'x':
        print('Good bye!')
        break
    try:
        int(isikukood)
        if len(isikukood) != 11:
            raise UserWarning
        if isikukood[0] in '09':
            raise Exception
    except ValueError:
        print('Code you entered is not numeric')
        continue
    except UserWarning:
        if len(isikukood) > 11:
            print('Code is too long')
        else:
            print('Code is too short')
        continue
    except Exception:
        print('First digit of ID is illegal!')
        continue
    else:
        while True:
            user_choice = input('1.Get gender\n'
                                '2.Get date of birth\n'
                                '3.Get region of birth\n'
                                '4.Validate ID\n'
                                '5.Change ID\n'
                                '0.Exit\n'
                                '--> ')
            if user_choice == '1':
                if int(isikukood[0]) % 2 == 0:
                    print('Female')
                else:
                    print('Male')
            elif user_choice == '2':
                bcent = ''
                if isikukood[0] in '12':
                    bcent = '18'
                elif isikukood[0] in '34':
                    bcent = '19'
                elif isikukood[0] in '56':
                    bcent = '20'
                elif isikukood[0] in '78':
                    bcent = '21'
                print(f'{isikukood[5:7]}.{isikukood[3:5]}.{bcent}{isikukood[1:3]}')
            elif user_choice == '3':
                if isikukood[0] in '5678':
                    if int(isikukood[1:3]) >= 13:
                        print('It is impossible to determine region for your ID code')
                        continue
                # CODE HERE #
            elif user_choice == '4':
                pass
            elif user_choice == '5':
                break
            elif user_choice == '0':
                print('Good bye!')
                exit()
            else:
                print('Choice is out of range!')
                continue
