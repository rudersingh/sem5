'''
wap to print a aquare pzttern of stars for n rows and n columns
'''
n = int(input("Enter rows and cols: "))
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()
