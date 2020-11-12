# *Define a collection of words, input 2 new words and add them to list, find some
# inputed word in list and remove a word with some inputed index

words = ['home', 'room', 'kitchen', 'bathroom', 'bedroom']
counter = 0
index = int(input('Write some number until ' + str(len(words)) + ': '))
while(counter < 2):
    words.append(input('Write some word about home: '))
    counter += 1
print(words)
print('Kitchen words index is: ', words.index('kitchen'))
del words[index]
print(words)