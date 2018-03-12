#write to a file and read it later

file_name = 'programming.txt'

with open(file_name, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run on a browser.\n")