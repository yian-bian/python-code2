# Part 2
# Author: Yian Bian
# Student ID: 260886212

from helpers import *

SPACE = '..\n..\n..'
HYPHEN = '..\n..\noo' 
APOSTROPHE = '..\n..\no.' 
QUOTES = '..\noo\noo'


############################ Functions

def convert_irregular(c):
    '''(str) -> str
    Convert the irregular characters to French Braille.

    >>> print(convert_irregular('-'))
    ..
    ..
    oo
    >>> convert_irregular('–')
    '..\\n..\\noo'
    >>> convert_irregular('`')
    '..\\n..\\no.'
    >>> convert_irregular("'")
    '..\\n..\\no.'
    >>> convert_irregular("’")
    '..\\n..\\no.'
    >>> convert_irregular("»")
    '..\\noo\\noo'
    '''
    # to see what type of irregular characters it belongs to
    # then convert it to French Braille
    if c == " ":
        return SPACE
    elif c == "-" or c == "–":
        return HYPHEN
    elif c == "`" or c == "'" or c == "’" or c ==", ":
        return APOSTROPHE
    elif c == "«" or c =="»":
        return QUOTES
    else:
        return None



def decade_pattern(decade_position):
    '''(int) -> str
    Using position in Braille decade, get associated Braille pattern.
    >>> decade_pattern(0)
    'o.\\n..'
    >>> decade_pattern(9)
    '.o\\noo'
    '''
    DEC_SEQ = ['o.\n..', 'o.\no.', 'oo\n..', 'oo\n.o',
           'o.\n.o', 'oo\no.', 'oo\noo', 'o.\noo',
           '.o\no.', '.o\noo']
    return DEC_SEQ[decade_position]


def convert_digit(c):
    '''(str) -> str
    Convert string representation of digit
    to Braille.
    >>> print(convert_digit('1'))
    o.
    ..
    ..
    >>> print(convert_digit('3'))
    oo
    ..
    ..
    >>> print(convert_digit('0'))
    .o
    oo
    ..
    '''
    if DIGITS.find(c) != -1:
         # to see if it's the right digit.
        return decade_pattern(int(DIGITS.find(c)))+"\n.."
    else:
        return None


def convert_punctuation(c):
    '''(str) -> str
    Convert string representation of common punctuation
    to French Braille.
    >>> print(convert_punctuation(','))
    ..
    o.
    ..
    >>> print(convert_punctuation(';'))
    ..
    o.
    o.
    >>> print(convert_punctuation(':'))
    ..
    oo
    ..
    >>> print(convert_punctuation('"'))
    ..
    oo
    oo
    '''
    if PUNCTUATION.find(c) != -1:
        # to see if it's the right punctuation
        return "..\n" + decade_pattern(int(PUNCTUATION.find(c)))
    else:
        return None

############################# 


def decade_ending(dec_num):
    '''(int) -> str
    For one of the four decades of standard letters in French Braille,
    return the associated bottom-row 
    >>> decade_ending(0)
    '..'
    >>> decade_ending(1)
    'o.'
    >>> decade_ending(2)
    'oo'
    >>> decade_ending(3)
    '.o'
    '''
    # find the correct and then return the corresponding bottom_row
    if dec_num == 0:
        return ".."
    elif dec_num == 1:
        return "o."
    elif dec_num == 2:
        return "oo"
    else:
        return ".o"


def letter_row(c):
    '''(str) -> int
    For a standard letter in French Braille, return
    the number of the decade it belongs to. (See table on page 3 of pdf.)
    Provided to students. Do not edit this function.

    >>> letter_row('a')
    0
    >>> letter_row('w')
    3
    >>> letter_row('n')
    1
    >>> letter_row('N')
    1
    '''
    c = c.lower() # convert
    for i, decade in enumerate(LETTERS):
        if c in decade:
            return i


def letter_column(c):
    '''(str) -> int
    For a standard letter in French Braille, return
    its position within its decade.
    >>> letter_column('a')
    0
    >>> letter_column('b')
    1
    >>> letter_column('v')
    1
    >>> letter_column('w')
    9
    >>> letter_column('W')
    9
    '''
    c = c.lower() # convert
    for decade in LETTERS:
        if c in decade:
            return decade.find(c)


def convert_letter(c):
    '''(str) -> str
    For one of the standard letters in French Braille,
    return its Braille representation.

    >>> print(convert_letter('a'))
    o.
    ..
    ..
    >>> print(convert_letter('b'))
    o.
    o.
    ..
    >>> print(convert_letter('p'))
    oo
    o.
    o.
    >>> print(convert_letter('ç'))
    oo
    o.
    oo
    >>> print(convert_letter('ô'))
    oo
    .o
    .o
    >>> print(convert_letter('A'))
    o.
    ..
    ..
    >>> print(convert_letter('Œ'))
    .o
    o.
    .o
    '''
    #First find the column and then convert it.
    #And begin a new line
    # at last convert the bottom row
    return decade_pattern(letter_column(c)) +"\n" + decade_ending(letter_row(c))


def char_to_braille(c):
    '''(str) -> str
    Convert a character, c, into French Braille.
    If c is a character we don't know how to convert, return 
    the same character as before.

    >>> print(char_to_braille('-'))
    ..
    ..
    oo
    >>> print(char_to_braille('w'))
    .o
    oo
    .o
    >>> print(char_to_braille('1'))
    o.
    ..
    ..
    >>> print(char_to_braille('?'))
    ..
    o.
    .o
    >>> char_to_braille('.')
    '..\\noo\\n.o'
    >>> char_to_braille('a')
    'o.\\n..\\n..'
    >>> char_to_braille('n')
    'oo\\n.o\\no.'
    >>> char_to_braille('Z')
    'o.\\n.o\\noo'
    >>> char_to_braille('Œ')
    '.o\\no.\\n.o'
    >>> char_to_braille(' ')
    '..\\n..\\n..'
    >>> char_to_braille('ß')
    'ß'
    >>> char_to_braille('\\n')
    '\\n'
    '''
    c = c.lower() #convert
    for decade in LETTERS:
        if is_letter(c) == True: # find if it's a letter
            return convert_letter(c) #convert
        elif IRREGULAR_CHARS.find(c) != -1:# to see if it's a irregular char
            return convert_irregular(c) #convert
        elif PUNCTUATION.find(c) != -1: # to see if it's a punctuation
            return convert_punctuation(c) # convert
        elif DIGITS.find(c) != -1: # to see if it's a digit
            return convert_digit(c) # convert
        else:
            return c


if __name__ == '__main__':
     doctest.testmod()
