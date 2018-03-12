# worldlist

worldlist = ['cat', 'dog', 'rabbit']
letterlist= []
for word in worldlist:
    #print(word)
    for letter in word:
        letterlist.append(letter)
print(letterlist)