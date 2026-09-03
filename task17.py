"""
Write a python program to take a student name and roll no then generate the user name using 
the first three letters of the name and last 2 digit of the roll no 
"""
name = input("Enter Name: ")
roll_no =  input("Enter rollNo: ")

user_name = (f"{name[:3] + roll_no[-2:]}")
print("Generated user name = ",user_name)