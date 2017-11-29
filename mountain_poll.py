#mountain poll.

responses = {}

#set a flag that indicate the polling is active
polling_active = True

while polling_active:
    #capture name and response
    name = input("\nWhat's your name? ")
    response = input("\nWhich candidate would you like to vote as a president? ")

    #store responses in a dictionary
    responses[name] = response

    #find out if anyone is going to take the poll.WHY? this will save as the break point 
    # otherwise the loop will be inifinity
    repeat = input("Would you like to let another person to respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

    #show the results
    print("\n --- Polling Results ---")
    for name, response in responses.items():
        print(name.title() + " would like to vote for " + response.title() + ".")
    
