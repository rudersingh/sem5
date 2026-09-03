"""
Write a python program to take 10 digit mobile no and display only the last 4 digits . 
Replace the first 6 digit with
"""
mobile = input("Enter mobile no: ")
masked ="******"+mobile[-4:]
print(masked)