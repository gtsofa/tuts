#greet a list of users individually.
def greet_user(names):
    #print a simple greeting to each user in a list
    for name in names:
        print("\n Hello, " + name.title() + "!")

usernames = ['tsofa', 'julius', 'nyule', 'sarah']
greet_user(usernames)