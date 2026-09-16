#write a python program to input marks of 10students.Store only valid marks between 0 and 100 in a list.Skip in valid marks
marks = []

for i in range(10):
    m = int(input("Enter marks: "))
    if 0 <= m <= 100:
        marks.append(m)

print(marks) 