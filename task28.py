#take roll no like 2024a1r057 and exact admission year , program code , and roll number digits using slicing.

roll = input ("Enter your roll number : ")

admission_year = roll[0:4]
batch_code = roll[4:6]
roll_number = roll[7:10]


print("Admission Year:" , admission_year)
print("Program Code:" , batch_code)
print("Roll Number:", roll_number)