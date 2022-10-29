### user input from the command line

import random
import sys

# Pick a random word from a provided list
def pick_random_word(list):
    return random.choice(list)

# Get a code name made up of the number of words specified
def get_code_name(list, num_words):
    if num_words.isdigit() == False:
        return 'Error: incorrect argument provided. You must provide an integer.'

    num_words = int(num_words)
    code_name = ''

# check if we have 2 arguments
    if sys.argv[2]:
        for x in range(1,num_words):
            word = pick_random_word(list)
            code_name += word + ' '
        code_name += must_include
    else:
        for x in range(1,num_words+1):
            word = pick_random_word(list)
            code_name += word + ' '

    return code_name.rstrip()

# List of words to use
word_list = ['Aurora', 'Avalanche', 'Blizzard', 'Cyclone', 'Eagle', 'Edison', 'Frost', 'Hawk', 'Hexagon', 'Hornet', 'Medusa', 'Neptune', 'Orion', 'Osprey', 'Plato', 'Portal', 'Raven', 'Sand', 'Shadow', 'Storm', 'Sunset', 'Thunder', 'Vector', 'Vista', 'Vortex', 'Volcano']

# Retrieve the command line argument
words_to_pick = sys.argv[1]
must_include = sys.argv[2]

# Create a code name and print it to the screen
code_name = get_code_name(word_list, words_to_pick)
print(code_name)