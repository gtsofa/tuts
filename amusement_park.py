#amusement park charges
"""
consider an amusement park that charges different rates for
different age groups:

Admission for anyone under age 4 is free.
Admission for anyone between the ages of 4 and 18 is $5.
Admission for anyone age 18 or older is $10.

How can we use an if statement to determine a person’s admission rate?

"""
age = 4
if age < 4:
    print("Your admission charge is kshs 0.")
elif age < 18:
    print("Your admission charge is kshs 500.")
else:
    print("Your admission charge is kshs 1000.")
