"""
Write a python program to store all month name in a tuple. Input a month number and display the 
corresponding month name
"""
months = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)
try:
    month_number = int(input("Enter a month number (1-12): "))
    if 1 <= month_number <= 12:
        print(f"The month is: {months[month_number - 1]}")
    else:
        print("Invalid number")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
