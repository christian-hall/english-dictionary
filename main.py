import json

print('Welcome to the English Dictionary Python Program')
print('Enter "1234" at any time to quit the program')

word, data = '', json.load(open('data.json', 'r'))
while word != '1234':
    word = input('Enter word: ')
    if word != '1234' and word in data:
        print(data[word])
    elif word != '1234' and word not in data:
        print('Word not found. Try again.')

print("Goodbye")
