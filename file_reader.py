#will read contents of pi

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)