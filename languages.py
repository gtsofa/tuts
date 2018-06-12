#using a set - to make elements in a set be unique.

favourite_languages = {
    'julius' : 'c#',
    'daktari' : 'python',
    'peter' : 'php',
    'eunice' : 'ruby',
}
print("The following languages have been mentioned:")
#set eliminate duplicate elements and make them unique.
for language in set(favourite_languages.values()):
    print(language.title())