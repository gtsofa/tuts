#requested toppings.
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:

#         print("Adding " + requested_topping + ".")

# print("\nFinished making your pizza.")

#multiple lists
"""
each item in requested_toppings is checked against the
list of available toppings before it’s added to the pizza:
"""
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorrry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza.")
