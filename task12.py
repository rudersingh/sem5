"""
Write a program to fill the template with name and date
"""

# name = input("Enter name: ")
# date =input("Enter Date: ")

# print(f"Dear {name},\nYou are selected for interview!\n{date}\nThank you")

letter = '''
Dear <Name>,
You are Selected!
<Date>
'''

name = input("Enter Name: ")
date = input("Enter Date: ")

letter = letter.replace("<Name>", name)
letter = letter.replace("<Date>", date)

print(letter)