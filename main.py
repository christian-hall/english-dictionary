import json

print('Welcome to the English Dictionary Python Program')

data = json.load(open('data.json', 'r'))


def definition(entry):
    return data[entry]


word = input("Enter word: ")

print(definition(word))
