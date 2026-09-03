"""
Take an email address and checkwhether it contains @ and .com
"""

email = input("Enter your email address: ")
if "@" in email and ".com" in email:
    print("Valid email address")
else:
    print("Invalid email address")