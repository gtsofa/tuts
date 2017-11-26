#using a set - to make elements in a set be unique.

favourite_languages = {
    'julius' : 'c#',
    'daktari' : 'python',
    'peter' : 'php',
    'eunice' : 'ruby',
}
print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())