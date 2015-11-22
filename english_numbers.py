import re


master_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
               'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
               'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
               'nineteen', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty',
               'seventy', 'eighty', 'ninety', 'hundred']


def naming_function(number):
    name_string = ""
    number = number[::-1].lstrip('0')
    if len(number) is 1:
        name_string += master_list[int(number[0])]
    elif len(number) is 2:
        if int(number[0]) is 1 or 0:
            name_string += master_list[int(number[:2])]
        else:
            name_string += master_list[int(number[0]) + 18] + ' '
            name_string += master_list[int(number[1])]
    elif len(number) is 3:
        name_string += master_list[int(number[0])] + ' ' + master_list[-1] + ' '
        if int(number[1]) is 1 or 0:
            name_string += master_list[int(number[1:])]
        else:
            name_string += master_list[int(number[1]) + 18] + ' '
            name_string += master_list[int(number[2])]

    return name_string.replace(" zero", "")


def english_numbers(number, function):
    english_word = []
    # Reverses a list in which each element is 3 digits or less
    number = number[::-1]
    list_of_reversed_number_strings = re.findall('...?|.', str(number))

    print(list_of_reversed_number_strings)
    # Applies
    for e, i in enumerate(list_of_reversed_number_strings):
        print('i: {}'.format(i))
        english_word.insert(0, function(i))
        if e is 1:
            print(english_word)
            english_word.insert(0, 'thousand')
        elif e is 2:
            english_word.insert(0, 'million')
        elif e is 3:
            english_word.insert(0, 'billion')
        elif e is 4:
            english_word.insert(0, 'trillion')

    return ' '.join(english_word)

print(english_numbers('1991999', naming_function))
