"""
Take a sentence containing double space and unwanted space at the beginning or end . clean the se
ntence and print the cleaned sentence
"""

sentence = input("Enter a sentence: ")
cleaned_sentence = ' '.join(sentence.split())
print("Cleaned sentence: ", cleaned_sentence)