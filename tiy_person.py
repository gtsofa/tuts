#dictionary containing person information
person = {'first_name':'julis', 'last_name':'tsofa', 'age':29, 'city':'watamu'}
print(person)
print("Your first name is "+ person['first_name'].title())
for key, value in person.items():
    print("\nKey: " + key)
    print("Value: " + str(value))

