"""
Write a python program to check whether the given value is present in a tuple, if present display
its position (0-based index)
"""
my_tuple = (1,2,3,4,5,6,7,8,9)
value = int(input("Enter value to search: "))
pos = -1
for i in my_tuple:
    if value == my_tuple[i]:
        pos = i 
        break
    
print(f"Position of the given value {value} is: ",pos)
