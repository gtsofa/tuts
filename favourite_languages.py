#dictionary containing a list
favourite_languages = {
    'julius': ['c#', 'ruby', 'python'],
    'sarah': ['statistics'],
    'daktari':['java', 'python'],
    'peter': ['php', 'photoshop', 'python'],
    }

for name, languages in favourite_languages.items():
    print("\n" + name.title() +"'s favourite languages are.")
    
    for language in languages:
        print(language.title())
        


