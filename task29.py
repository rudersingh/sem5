student_name = input ("Enter name: ")
branch_name= input("Enter branch: ")
year= input("Enter year: ")

code_name = student_name[:3] + "-" + branch_name[:3] + "-" +year [-2:]

print("*" * 30)
print("Student Code:", code_name)
print("*" *30)