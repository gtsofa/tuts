
def get_formatted_name(first_name, last_name, middle_name=""):
    """Generate a neatly formatted full name"""
    if middle_name == '':#if middle_name:
        full_name = first_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    #print(full_name.title())
    return full_name.title()
    
#get_formatted_name('tsofa', 'nyule', 'julius')
#get_formatted_name('sarah', 'munga')
#get_formatted_name('samuel', 'baya', 'kitsao')