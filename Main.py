def Main():
    while True:
        print('Welcome to Infinity Students Portal!')
        print('\nWhat do you want to do? ')
        choice = int(input('\n1. Register. \n2. Log in. \n3. Contact Us. \n4. Exit'))

        if choice == 1:
            try:
                fname = input('Enter your first name: ')
                lname = input('Enter you Surname: ')

                new = class(Registration)

        elif choice == 2:
            Login()

        elif choice == 3:
            filename = 'contact.txt'
            with open(filename) as contents:
                print(contents.read())
        else:
            answer = input('Are you sure you want to Exit? ')
            if answer == "yes":
                break
            else:
                print('Thank you for choosing Infinity Private School!')


Main()
