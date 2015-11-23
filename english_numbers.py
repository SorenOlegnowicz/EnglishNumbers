import re


master_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
               'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
               'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
               'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
               'seventy', 'eighty', 'ninety', 'hundred']


def naming_function(number):
    name_string = ""
    number = number[::-1].lstrip('0')
    if len(number) is 1:
        name_string += master_list[int(number[0])]
    elif len(number) is 2:
        if int(number[0]) is 0 or int(number[0]) is 1:
            name_string += master_list[int(number[:2])]
        else:
            name_string += master_list[int(number[0]) + 18] + ' '
            name_string += master_list[int(number[1])]
    elif len(number) is 3:
        # Hundred's place
        name_string += master_list[int(number[0])] + ' ' + master_list[-1] + ' '
        # Ten's and/or one's place
        if int(number[1]) is 0 or int(number[0]) is 1:
            name_string += master_list[int(number[1:])]
        else:
            # Ten's
            name_string += master_list[int(number[1]) + 18] + ' '
            # One's
            name_string += master_list[int(number[2])]

    return name_string.replace(" zero", "")


def english_numbers(number, function):
    english_word = []
    # Strips any leading zeros
    number = number.lstrip('0')
    # Reverses a list in which each element is 3 digits or less
    number = number[::-1]
    list_of_reversed_number_strings = re.findall('...?|.', str(number))
    # Applies
    for e, i in enumerate(list_of_reversed_number_strings):
        print('i: {}'.format(i))
        if e is 1:
            english_word.insert(0, 'thousand')
        elif e is 2:
            english_word.insert(0, 'million')
        elif e is 3:
            english_word.insert(0, 'billion')
        elif e is 4:
            english_word.insert(0, 'trillion')
        #   naming_function()
        english_word.insert(0, function(i))
    # turns list into string
    english_word = ' '.join(english_word)
    # returns string adjusted for place redundancy
    return english_word.split('  ')[0]
