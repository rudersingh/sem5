"""
Write a python program to take a word and print it in reverese order using slicing . Also 
check whether it is the same forwoard and backward.
"""

word = input("Enter word: ")
reverse_word = word[::-1]
print("Reversed word : ", reverse_word)
print("result ", word == reverse_word)