#nesting a dictionary in a dictionary.
users = {
    'maestro': {
        'firstname': 'tsofa',
        'lastname': 'nyule',
        'location': 'watamu',
    },
    'smunga': {
        'firstname': 'sarah',
        'lastname': 'munga',
        'location': 'dam estate',
    },
    'daktari': {
        'firstname': 'james',
        'lastname': 'dindi',
        'location': 'busia',
    },
    'pish': {
        'firstname': 'peter',
        'lastname': 'wafula',
        'location': 'dooni',
    },

}

for username, user_info in users.items():
    print("\n Username: " + username)
    #print("Full name: " + user_info['firstname'].title() +" " + user_info['lastname'].title())
    #refactor code
    full_name = user_info['firstname'] + " " + user_info['lastname']
    print("Full name: " + full_name.title())
    #refactor code to make it readable
    #print("Location: " + user_info['location'].title())
    location = user_info['location']
    print("Location: " + location.title())

