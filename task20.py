"""
Write a python program to take a word and count the number of vowels 
"""
word = input("Enter word: ")
count = word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")
print("Total vowels : ",count) 