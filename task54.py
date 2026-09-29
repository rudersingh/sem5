"""
Write a Python program to show that tuple value cannot be changed directly. Convert tuple into list
update it and convert again into list
"""
my_tuple = ("apple","mango","orange")
lists = list(my_tuple)
# Update a list
lists.insert(1,"banana")
my_tuple = tuple(lists)
print(my_tuple)
