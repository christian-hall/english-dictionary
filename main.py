import json
from difflib import get_close_matches as close_matches

print('Welcome to the English Dictionary Python Program')
print('Enter a blank at any time to quit the program')

word, data = ' ', json.load(open('data.json', 'r'))
while word != '':
    word = input('Enter word: ').lower()
    if word == '':
        pass
    elif word in data:
        print(str(data[word]))
    elif word not in data:
        autocorrect = close_matches(word, data.keys())
        if autocorrect:
            for suggestion in autocorrect:
                corrected_word = input(f'Did you mean "{suggestion}"? (y/n): ')
                if corrected_word == 'y':
                    print(str(data[suggestion]))
                    break
            else:
                print('Word not found. Try again.')

        else:
            print('Word not found. Try again.')

print("Goodbye")
