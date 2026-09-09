#write a python program to create a simple password validation system 
'''
the program should repeatedly ask the user to enter a password until a valid password is entered.A password willbe considered valid only if it has at least 8 characters and contains the @ symbol
once a user enters a valid password ,the program should display "Password accepted "
and stop otherwise,
it should display "Weak password try again and ask for the password again
'''

while True:
    password = input ("Enter your password: ")

    if len(password) >=8 and "@" in password:
        print ("Password accepted")
    else:
        print("weak password,try again")