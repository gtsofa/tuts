#while loop implementation

prompt = "\n Tell me something that i will not forget."
prompt += "\n enter 'quit' to end the program. " 

active = True

while active:
    message = input(prompt)


    if message == 'quit':
        active = False
    else:
        print(message)
            
        
    


