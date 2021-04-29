import json
from difflib import get_close_matches as close_matches

print('Welcome to the English Dictionary Python Program')
print('Enter "0" at any time to quit the program')

word, data = ' ', json.load(open('data.json', 'r'))
while word != '0':
    word = input('Enter word: ').lower()
    if word == '0':
        pass
    elif word in data:
        output = data[word]
    elif word not in data:
        autocorrect = close_matches(word, data.keys())
        if autocorrect:
            for suggestion in autocorrect:
                corrected_word = input(f'Did you mean "{suggestion}"? (y/n): ')
                if corrected_word == 'y':
                    output = data[suggestion]
                    break
            else:
                output = 'Word not found. Try again.'
        else:
            output = 'Word not found. Try again.'
    if output.type == list:
        for definition in output:
            print(definition)
    else:
        print(output)
print("Goodbye")
