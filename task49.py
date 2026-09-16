'''
wap to print the following patterns for n rows
1
12
123
1234
'''
n = int(input("Enter rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
