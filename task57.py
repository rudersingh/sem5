"""
Write a python program to store a student data as a tuple: name , roll no and marks 
Display grade based on marks                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
"""
student_data = ("Alex Morgan", 101, 85)
name, roll_no, marks = student_data
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"
    
print(f"Name:        {name}")
print(f"Roll Number: {roll_no}")
print(f"Marks:       {marks}%")
print(f"Grade:       {grade}")
