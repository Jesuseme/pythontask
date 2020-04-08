import random
import string

user_list = []


def main():
    # separates the first two letters of the first name
    def first_two(first_name):
        global f_two
        f_two = first_name[0:2]
        return f_two

    # separates the last two letters of the last name
    def last_two(last_name):
        global l_two
        l_two = last_name[-2:]
        return l_two

    # generates the password using the values from the first two functions with 5 randomly generated lowercase letters
    def password_gen():
        first_two(first_name)
        last_two(last_name)
        length = 5
        random.choice(string.ascii_lowercase)
        a = ''.join(random.choice(string.ascii_lowercase) for i in range(length))
        global new_password
        new_password = f_two + l_two + a
        password_assign(new_password)

    # shows the user the generated password and changes it if not suitable
    def password_assign(new_password):
        print('This is your auto generated password:')
        print(new_password)
        print('Are you satisfied with the password:')
        ok = input('Y/N: ')
        if ok == 'Y' or ok == 'y':
            full_details()

        elif ok == 'N' or ok == 'n':
            print('Enter your preferred password:')
            inputed_password = input()
            # makes sure password is more than 6 characters
            if len(inputed_password) > 6:
                # reassigns the global variable with the new inputed password
                listOfGlobals = globals()
                listOfGlobals['new_password'] = inputed_password
                print('new password saved')
                full_details()
                return new_password

            elif len(inputed_password) < 7:
                print('password must be have more than six characters')
                password_gen()

        else:
            print('invalid input')

    def full_details():
        print('Registration complete. kindly take note of your details')
        print('------------------------------------------------------')
        print("Full name: " + first_name + " " + last_name)
        print("Email Address: " + email)
        print("Account password: " + new_password)

        new_user = {'firstName': first_name, 'LastName': last_name, 'emailAddress': email,
                    'AccountPassword': new_password}
        user_list.append(new_user)

        print("--------------------------------------------")
        print("set up complete")
        print("--------------------------------------------")
        print('press 1 to end program or press 2 to create another account')
        new_account = input('1 or 2: ')
        if new_account == '1':
            print(user_list)
            print('good bye')
        elif new_account == '2':
            main()

    print('-------------------------------------------------------')
    print('-------------------------------------------------------')
    print('Welcome to hng, lets get you set up shall we')
    print('please fill in your details below:')
    first_name = input('First name:')
    last_name = input('last name:')
    email = input('Email:')
    print('------------------------------------------------------')
    print(first_name + ' ' + last_name + ' ' + email)
    print('------------------------------------------------------')
    print('please confirm that your details are correct')
    print('press 1 to proceed, 2 to re-enter details:')
    proceed = input()
    if proceed == '1':
        print('------------------------------------------------------')
        password_gen()
    elif proceed == '2':
        print('please, take your time and carefully re-enter details')
        print('------------------------------------------------------')
        print('------------------------------------------------------')
        main()
    else:
        print('Please enter valid code')


main()
