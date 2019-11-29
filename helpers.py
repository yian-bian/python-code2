# Part 1
# Author: Yian Bian
# Student ID: 260886212

import doctest


# These constants are for you to use
IRREGULAR_CHARS = " -–`'’«»"
DIGITS = '1234567890'
PUNCTUATION = ',;:.?!"(*)' 

LETTERS = ['abcdefghij', 
           'klmnopqrst', 
           'uvxyzçéàèù',
           'âêîôûëïüœw'] 

################ Functions


def is_in_decade(c, decade):
    '''(str, str) -> bool
    Return whether c is a single-letter character contained within decade.

    >>> is_in_decade('a', 'abcdefghij')
    True
    >>> is_in_decade('z', 'abcdefghij')
    False
    >>> is_in_decade('a', 'âêîôûëïüœw')
    False
    >>> is_in_decade('âêî', 'âêîôûëïüœw')
    False
    '''
    length = len(c) #to see the number of characters
    position_of_c = decade.find(c) # to see if c is contained within decade
    if position_of_c == -1 or length != 1: #if n = -1 then c is not in the decade, if m != 1 the c is not a single word
        return False
    else:
        return True
    


def is_irregular(c):
    '''(str) -> bool
    Return whether character c is a single one of the irregular characters
    in French Braille.

    >>> is_irregular(' ')
    True
    >>> is_irregular('’')
    True
    >>> is_irregular(')')
    False
    >>> is_irregular('-')
    True
    >>> is_irregular('`')
    True
    >>> is_irregular("'")
    True
    >>> is_irregular('a')
    False
    >>> is_irregular('')
    False
    >>> is_irregular('1')
    False
    >>> is_irregular('«»')
    False
    >>> is_irregular('(1-1)')
    False
    '''
    length = len(c) # to see the number of characters
    position_of_c = IRREGULAR_CHARS.find(c) # to find the position of c in IRREGULAR_CHARS
    # to see if c is a single letter and is contained in IRREGULAR_CHARS at the same time
    if position_of_c == -1 or length != 1: 
        return False
    else:
        return True


def is_digit(c):
    '''
    (str) -> bool
    Return whether character c represents a single digit.
    >>> is_digit('2')
    True
    >>> is_digit('0')
    True
    >>> is_digit('12')
    False
    '''
    length = len(str(c))# to see the number of characters
    position_of_c = DIGITS.find(str(c)) # to find the position of c in DIGITS
    # to see if c is a single letter and is contained in DIGITS at the same time
    if position_of_c == -1 or length != 1:
        return False
    else:
        return True


def is_punctuation(c):
    '''(str) -> bool
    Return whether c is a single character that is one of the common, regular
    forms of punctuation in French Braille.
    >>> is_punctuation(',')
    True
    >>> is_punctuation(',,')
    False
    >>> is_punctuation('-')
    False
    >>> is_punctuation('"')
    True
    >>> is_punctuation('')
    False
    >>> is_punctuation('a')
    False
    '''
    length = len(c) # to see the number of characters
    position_of_c = PUNCTUATION.find(c) # to find the position of c in DIGITS
    # to see if c is a single letter and is contained in PUNCTUATION at the same time
    if position_of_c == -1 or length != 1:
        return False
    else:
        return True


def is_letter(c):
    '''(str) -> bool
    Return whether c is a single one of one of the standard letters
    in French Braille.
    >>> is_letter('a')
    True
    >>> is_letter('z')
    True
    >>> is_letter('w')
    True
    >>> is_letter('é')
    True
    >>> is_letter('A')
    True
    >>> is_letter('Œ')
    True
    >>> is_letter('1')
    False
    >>> is_letter('ß')
    False
    >>> is_letter('aa')
    False
    >>> is_letter('Hello')
    False
    '''
    c = c.lower()
    for decade in LETTERS:
        if is_in_decade(c, decade):
            return True
    return False


def is_known_character(c):
    '''
    (str) -> bool
    Is c one of the characters supported by French Braille?
    (Letter, digit, punctuation or irregular.)

    >>> is_known_character('a')
    True
    >>> is_known_character('É')
    True
    >>> is_known_character('-')
    True
    >>> is_known_character('4')
    True
    >>> is_known_character('.')
    True
    >>> is_known_character('@')
    False
    >>> is_known_character('ß')
    False
    >>> is_known_character('\\n')
    False
    '''
    # to see if c is one of the characters in irregular
    if is_irregular(c) is True:
        return True
    # if c is not in irregular then tests is it's in digit
    elif is_digit(c) is True:
        return True
    # to see if c is contained in punctuation
    elif is_punctuation(c) is True:
        return True
    # to see if it's in letters
    elif is_letter(c) is True:
        return True
    else:
        return False



def is_capitalized(c):
    '''
    (str) -> bool
    Return whether c is a single capitalized letter supported by French Braille.

    >>> is_capitalized('A') 
    True
    >>> is_capitalized('a')
    False
    >>> is_capitalized('W')
    True
    >>> is_capitalized('É')
    True
    >>> is_capitalized(' ')
    False
    >>> is_capitalized('')
    False
    >>> is_capitalized('Δ')
    False
    >>> is_capitalized('femmes')
    False
    >>> is_capitalized('FEMMES')
    False
    '''
    #to see if c is the capital letters or some things like puntuation,small letters, digits and irregular chars
    if c == c.lower():
        return False
    #if it's capital, then tests if it's a single character in suppouted by French Braille 
    elif is_letter(c) == False:
        return False
    else:
        return True
    


#########################################

if __name__ == '__main__':
    doctest.testmod()
