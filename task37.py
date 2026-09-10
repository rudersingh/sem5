credentials1 = "2024A1R040@MIETJAMMU.IN" 
credentials2 = "Ruder@123"
count = 3
while count > 0:
    email = input("Enter Email: ").upper()
    password = input("Enter Password: ")

    if email == credentials1 and password == credentials2:
        print("Login successful")
        break
    else:
        count -= 1
        if count > 0:
            print(f"Incorrect credentials. You have {count} attempts left.\n")
        else:
            print("Account Locked")