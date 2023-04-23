print("Welcome User! ")


# The menu function
def menu():
    while True:
        try:
            # Displaying the menu
            print("\nMENU")
            print('\n' + '1. Log in \n2. Register \n3. contact us \n4. Exit')
            choice = int(input('what do you want to do : '))

            # First choice
            if choice == 1:
                email_check()
                password_check()

            # Second choice

            elif choice == 2:
                firstname = input('Enter your firstname: ')
                surname = input('Enter your Surname: ')
                email_check()
                gender()
                print('\nEnter you birthday starting from year, month and day below.. ')

                # converting the year entered into an integer number
                while True:
                    try:
                        year = int(input('\nYear: '))

                        if year > 0 and year != 0:
                            # checking if the year is Leap.
                            if year % 4 == 0 and year % 100 != 0:
                                leapyear()
                                break
                            # Not a leap year
                            else:
                                not_leapyear()
                                break
                        else:
                            print('A year can not be negative')
                    except:
                        print('Please re-enter the year!')
                country_check()
                password_check()


            # third choice
            elif choice == 3:
                print('For inquiries or comments, \n')
                print('Contact us on: +265994679974' + '\nOr' + '\nEmail: kelvinmponda47@gmail.com' + '\nThank you!')

            # fourth choice
            elif choice == 4:
                print('\nThank you for using our services!')
                break

            # If user enters other choice
            else:
                print('Error! \nPlease enter the correct choice')

        except:
            print('Please enter the correct choice')


# Checking an email
def email_check():
    while True:
        print('\nHint: Use a google or yahoo account only')
        check = input('Enter your email here: ')
        length = len(check)

        if check[length - 10:] == '@gmail.com' or check[length - 10:] == '@yahoo.com':
            break
        else:
            print('Error in entering the email, Please re-enter!')


# checking the password
def password_check():
    while True:
        password = input('Hint: Your password should have at least 8 characters.' +
                         '\nEnter you password here: ')
        # checking the password length
        if len(password) >= 8:
            second = input('Re-enter to password to confirm: ')
            # confirming the password
            if second == password:
                # checking the characters of the password
                print('Password confirmed!')
                break
            else:
                print('Incorrect password entered, \nEnter the password again!')
        else:
            print('Incorrect password entered, \nEnter the password again!')


# checking the gender
def gender():
    while True:
        sex = input('Enter your gender here: ')
        if sex == 'male' or 'female':
            break
        else:
            print('\nYou have entered an incorrect gender.')


# if is a normal year
def not_leapyear():
    while True:

        try:
            # Entering the month
            month = int(input('Enter month: '))
            months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

            # Entering the day
            day = int(input('Enter Day: '))
            days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                    28]  # The days of february
            days1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                     28, 29, 30]  # Months with 30 days
            days2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                     28, 29, 30, 31]  # Months with 31 days
            i = 0
            # January(31 days)
            if month == months[0]:
                while i <= len(days2):

                    if day == days2[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # February(28 days)
            elif month == months[1]:
                while i <= len(days):
                    if day == days[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # March(31 days)
            elif month == months[2]:
                while i <= len(days2):
                    if day == days2[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # April(30 days)
            elif month == months[3]:
                while i <= len(days1):
                    if day == days1[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # May(31 days)
            elif month == months[4]:
                while i <= len(days2):
                    if day == days2[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # June(30 days)
            elif month == months[5]:
                while i <= len(days1):
                    if day == days1[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # July(31 days)
            elif month == months[6]:
                while i <= len(days2):
                    if day == days2[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # August(31 days)
            elif month == months[7]:
                while i <= len(days2):
                    if day == days2[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # Sept(30 days)
            elif month == months[8]:
                while i <= len(days1):
                    if day == days1[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # October(31 days)
            elif month == months[9]:
                while i <= len(days2):
                    if day == days2[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # November(30 days)
            elif month == months[10]:
                while i <= len(days1):
                    if day == days1[i]:
                        print('Date successfully entered!')
                        break

                    else:

                        i += 1
                break
            # December(31 days)
            elif month == months[11]:
                while i <= len(days2):
                    if day == days2[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1

            else:
                print('Enter the correct month!')
        except:
            print('Enter the correct date')


# if the year is leaped
def leapyear():
    while True:

        try:
            # Entering the month
            month = int(input('Enter month: '))
            months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

            # Entering the day
            day = int(input('Enter Day: '))
            days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                    28, 29]  # The days of february
            days1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                     28, 29, 30]  # Months with 30 days
            days2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                     28, 29, 30, 31]  # Months with 31 days
            i = 0
            # January(31 days)
            if month == months[0]:
                while i <= len(days2):

                    if day == days2[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # February(28 days)
            elif month == months[1]:
                while i <= len(days):
                    if day == days[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # March(31 days)
            elif month == months[2]:
                while i <= len(days2):
                    if day == days2[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # April(30 days)
            elif month == months[3]:
                while i <= len(days1):
                    if day == days1[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # May(31 days)
            elif month == months[4]:
                while i <= len(days2):
                    if day == days2[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # June(30 days)
            elif month == months[5]:
                while i <= len(days1):
                    if day == days1[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # July(31 days)
            elif month == months[6]:
                while i <= len(days2):
                    if day == days2[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # August(31 days)
            elif month == months[7]:
                while i <= len(days2):
                    if day == days2[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # Sept(30 days)
            elif month == months[8]:
                while i <= len(days1):
                    if day == days1[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # October(31 days)
            elif month == months[9]:
                while i <= len(days2):
                    if day == days2[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1
                break
            # November(30 days)
            elif month == months[10]:
                while i <= len(days1):
                    if day == days1[i]:
                        print('Date successfully entered!')
                        break

                    else:

                        i += 1
                break
            # December(31 days)
            elif month == months[11]:
                while i <= len(days2):
                    if day == days2[i]:
                        print('Date successfully entered!')
                        break
                    else:

                        i += 1

            else:
                print('Enter the correct month!')
        except:
            print('Enter the correct date')


# checking the country and verifying a phone number
def country_check():
    while True:
        # entering the country of residence
        country = input('Enter your country of residence: ')

        # checking the country and entering a phone number
        if country == 'Malawi':
            phone_number = input('Enter your number number starting with your country code: ')

            if phone_number[:4] == '+265' and len(phone_number) == 13:
                print('Phone number verified!')
                break
            else:
                print('You have entered an invalid phone number..')
        else:
            nationality = input('Please specify your nationality: ')
            break


menu()
