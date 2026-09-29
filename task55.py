"""
Write a python program to store repeated values in a tuple and count how many times a given value
appear
"""
my_tuple = (1,2,3,1,2,3,4,5,2)
value = int(input("Enter a value: "))
count = 0
length = len(my_tuple)
for i in range(0,length):
    if(my_tuple[i] == value):
        count += 1
        
print("Frequency: ",count)
        
