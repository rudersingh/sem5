"""
write a python program to take a string and seperate character present at even index
position and odd index position
"""

text = input("Enter string: ")
even_chars = text[::2]
odd_chars = text[1::2]
print("Even index characters : ", even_chars)
print("Odd index characters : ", odd_chars)