#while loop implementation

prompt = "\n Tell me something that i will not forget."
prompt += "\n enter 'quit' to end the program. " 

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)


