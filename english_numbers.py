import re


def naming_function(number):
    pass


def english_numbers(number, function):
    english_word = []
    # Reverses a list in which each element is 3 digits or less
    list_of_reversed_number_strings = [x[::-1] for x in re.findall('...?|.', str(number))]
    # Applies
    for e, i in enumerate(list_of_reversed_number_strings):
        english_word.insert(function(i), 0)
        if e is 1:
            enlgish_word.insert('thousand', 0)
        elif e is 2:
            enlgish_word.insert('million', 0)
        elif e is 3:
            enlgish_word.insert('billion', 0)
        elif e is 4:
            enlgish_word.insert('trillion', 0)

    return enlgish_word.join(' ')

print(english_numbers(5001235121))
