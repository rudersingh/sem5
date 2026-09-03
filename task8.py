""" Write a python program to calculate simple interest and total amount using principle , rate and time entered by the user """

principle = float(input("Enter Principle: "))
rate = float(input("Enter annual interest rate (in %): "))
time_minutes = float(input("Enter time in minutes: "))

time_years = time_minutes / 525600

simple_interest = (principle * rate * time_years) / 100

total_amount = principle + simple_interest

print(f"Simple Interest: {round(simple_interest, 2)}")
print(f"Total Amount: {round(total_amount, 2)}")