"""
write a python program to take a student full name and display 
Total number of characters , First characters , Last characters , Name in uppercase form
"""

Name = input("Enter name: ")
print("first character: ",Name[0])
print("last character: ",Name[-1])
print("total characters: ",len(Name))
print("name in uppercase: ",Name.upper())