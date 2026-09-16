n = int(input("Enter number of elements: "))
a = list(map(int, input("Enter numbers: ").split()))

a = list(set(a))
a.sort()

print("Second largest number:", a[-2])
