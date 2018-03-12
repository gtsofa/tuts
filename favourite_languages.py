#dictionary containing a list

from collections import OrderedDict

favourite_languages = OrderedDict()

favourite_languages['julius'] = 'c#'
favourite_languages['sarah'] = 'stats'
favourite_languages['daktari'] = 'java'

# favourite_languages = {
#     'julius': ['c#', 'ruby', 'python'],
#     'sarah': ['statistics'],
#     'daktari':['java', 'python'],
#     'peter': ['php', 'photoshop', 'python'],
#     }

for name, languages in favourite_languages.items():
    if len(languages) <= 1:
        print("\n" + name.title() + "'s favourite language is:")
        
    else:
        print("\n" + name.title() +"'s favourite languages are:")
     
    for language in languages:
        print("*" + language.title())
        


