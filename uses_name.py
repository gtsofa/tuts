#this program uses the get_formatted_name()

from name import get_formatted_name

print("Enter 'q'  to quit")
while True:
    first_name = input("\nEnter your first name:")
    if first_name == 'q':
        break
    last_name = input("\n Enter your last name:")
    if last_name == 'q':
        break

    formatted_name = get_formatted_name(first_name, last_name)
    print("\tNeatly formatted name: " + formatted_name)