"""
Name: Brendan Kratt
lab1.py

Problem:
This program calculates the monthly interest charge for a credit card.
In-line citations should explain further.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

print("This program calculates the monthly interest rate for a credit card.")
print()

# Desired input: Percentage rate without % sign, i.e. float
apr = eval(input("What is the annual interest rate? "))
number_days = eval(input("How many days are in the billing cycle? "))
prior_bal = eval(input("What is the net balance? "))
payment_amt = eval(input("What is the payment amount? "))
day_of_payment = eval(input("What is the day in which you are making the payment? "))

"""
This could be made with fewer lines / more complex calculations, but doing so would make it prone to rounding errors.
The program has also been broken into several lines to increase readability. Steps 1-3 could  be done on a single line.
I've used particularly wordy variables in order to increase readability. If doing so is a handicap, let me know.
"""

step1 = prior_bal * number_days
step2 = payment_amt * (number_days - day_of_payment)
avg_daily_bal = (step1 - step2) / number_days

# APR / 12 = monthly %, but APR / 1200 = monthly in a calculable form
monthly_interest_rate = apr / 1200
monthly_interest_charge = avg_daily_bal * monthly_interest_rate

# String concatenation! If that's a bogeyman, let me know.
print("Your monthly interest charge is", '$' + str(monthly_interest_charge))


