# Part 4
# Author: Yian Bian
# Student ID: 260886212

from char_to_braille import *
from to_unicode import *
import filecmp

CAPITAL = '.o\n..\n.o' # is doubled for all caps
NUMBER = '.o\n.o\noo' 


#################################

def is_all_caps(s):
    '''(str) -> bool
    Return true if all characters of s are capital letters
    that are supported by our Braille translator, and
    there are at least two such letters.

    >>> is_all_caps('HA')
    True
    >>> is_all_caps('CHAT')
    True
    >>> is_all_caps('CHATte')
    False
    >>> is_all_caps('chAT')
    False
    >>> is_all_caps('ΓΆΤΑ')
    False
    >>> is_all_caps('123')
    False
    >>> is_all_caps('chat')
    False
    >>> is_all_caps('H')
    False
    >>> is_all_caps('COMP202')
    False
    >>> is_all_caps('')
    False
    >>> is_all_caps(':')
    False
    '''
    a = 0 # set the number to count
    if s == "": # to see if s is blank
        return False
    for i in range(int(len(s))):
        # to see whether s is all capital letters and there are at least two
        if s.upper() == s and len(s) >= 2 and is_letter(s[i]) == True:
            a += 1
            if a == len(s): # to end the loop
                return True
        else:
            return False


def word_to_braille(word):
    '''(str) -> str
    Given a string with no spaces and no newlines, convert to a Braille o-string.
    Put two newlines in between every Braille cell.
    The print_ostrint function we use in the doctest is to make the output more readable.

    >>> word_to_braille('hi')
    'o.\\noo\\n..\\n\\n.o\\no.\\n..\\n\\n'
    >>> print_ostring(word_to_braille('femmes'))
    oo o. oo oo o. .o
    o. .o .. .. .o o.
    .. .. o. o. .. o.
    >>> print_ostring(word_to_braille('Comment'))
    .o oo o. oo oo o. oo .o
    .. .. .o .. .. .o .o oo
    .o .. o. o. o. .. o. o.
    >>> print_ostring(word_to_braille('123'))
    .o o. .o o. .o oo
    .o .. .o o. .o ..
    oo .. oo .. oo ..
    >>> print_ostring(word_to_braille('hElL0!'))
    o. .o o. o. .o o. .o .o ..
    oo .. .o o. .. o. .o oo oo
    .. .o .. o. .o o. oo .. o.
    >>> print_ostring(word_to_braille('CHAT'))
    .o .o oo o. o. .o
    .. .. .. oo .. oo
    .o .o .. .. .. o.
    >>> print_ostring(word_to_braille('cCHAT'))
    oo .o oo .o o. .o o. .o .o
    .. .. .. .. oo .. .. .. oo
    .. .o .. .o .. .o .. .o o.
    >>> print_ostring(word_to_braille('cCHATte'))
    oo .o oo .o o. .o o. .o .o .o o.
    .. .. .. .. oo .. .. .. oo oo .o
    .. .o .. .o .. .o .. .o o. o. ..
    >>> print_ostring(word_to_braille('COMP202'))
    .o oo .o o. .o oo .o oo .o o. .o .o .o o.
    .. .. .. .o .. .. .. o. .o o. .o oo .o o.
    .o .. .o o. .o o. .o o. oo .. oo .. oo ..
    '''
    braille = "" # to create another string
    if is_all_caps(word): # to see if it's all capital letters
        for i in range(len(word)):
            # first convert all letters to braille
            braille += char_to_braille(word[i])+"\n\n"
            # then add the braille for the string that contains only capital letters
        return (CAPITAL+"\n\n")*2+braille
    for i in range(len(word)):
        if is_digit(word[i]):
            # first see whether it is digit
            # if it is then add the braille for digits before every digit
            braille += NUMBER+"\n\n"+char_to_braille(word[i])+"\n\n"
        else: # if it'is not all capital string either digits
            if is_capitalized(word[i]):
            # if there is only one capital letter
                braille += CAPITAL+"\n\n"+char_to_braille(word[i])+"\n\n"
            else: # just convert the character to braille
                braille += char_to_braille(word[i])+"\n\n"
    return braille
           


        

#################################


def print_ostring(braille_ostring):
    '''(str) -> NoneType
    Print a braille-converted o-string so
    all the top rows are at the top, mid in middle, and bottom
    at bottom. Assume two newlines between cells.
    >>> print_ostring('o.\\n..\\n..\\n\\no.\\no.\\n..\\n\\noo\\n..\\n..')
    o. o. oo
    .. o. ..
    .. .. ..
    >>> print_ostring('o.\\noo\\n..\\n\\n.o\\no.\\n..')
    o. .o
    oo o.
    .. ..
    >>> print_ostring(word_to_braille('ÉLEVÉ'))
    .o .o oo o. o. o. oo
    .. .. oo o. .o o. oo
    .o .o oo o. .. oo oo
    >>> print_ostring(word_to_braille(':PAR'))
    .. .o oo .o o. .o o.
    oo .. o. .. .. .. oo
    .. .o o. .o .. .o o.
    '''

    top_row = []
    mid_row = []
    low_row = []
    for b in braille_ostring.split('\n\n'):
        if b:
            cell_rows = b.split('\n')
            top_row.append(cell_rows[0])
            mid_row.append(cell_rows[1])
            low_row.append(cell_rows[2])

    print(*top_row, sep=' ')
    print(*mid_row, sep=' ')
    print(*low_row, sep=' ')


def paragraph_to_unicode(braille_ostring):
    '''(str) -> str
    Given a multi-cell braille o-string, convert it to unicode.
    There are two newlines in between each braille o-string cell.
    For readibility, replace ⠀ with space.

    >>> la_lune = '.o\\n..\\n.o\\n\\no.\\no.\\no.\\n\\no.\\n..\\n..\\n\\n..\\n..\\n..\\n\\no.\\no.\\no.\\n\\no.\\n..\\noo\\n\\noo\\n.o\\no.\\n\\no.\\n.o\\n..\\n\\n'
    >>> paragraph_to_unicode(la_lune)
    '⠨⠇⠁ ⠇⠥⠝⠑'
    >>> paragraph_to_unicode(paragraph_to_braille('123'))
    '⠼⠁⠼⠃⠼⠉'
    >>> paragraph_to_unicode(paragraph_to_braille('hElL0!'))
    '⠓⠨⠑⠇⠨⠇⠼⠚⠖'
    >>> paragraph_to_unicode(paragraph_to_braille('COMP 202'))
    '⠨⠨⠉⠕⠍⠏ ⠼⠃⠼⠚⠼⠃'
    >>> paragraph_to_unicode(paragraph_to_braille('BONJOUR la monde'))
    '⠨⠨⠃⠕⠝⠚⠕⠥⠗ ⠇⠁ ⠍⠕⠝⠙⠑'
    '''
    s = ''
    words = braille_ostring.split('\n\n')
    for c in words:
        s += ostring_to_unicode(c)
    s = s.replace('⠀', ' ')
    return s


######################################

def paragraph_to_braille(paragraph):
    '''(str) -> str
    Given a French text with no newlines in it, convert it to a braille o-string
    where two newlines separate each cell.

    >>> print_ostring(paragraph_to_braille('Comment les femmes'))
    .o oo o. oo oo o. oo .o .. o. o. .o .. oo o. oo oo o. .o
    .. .. .o .. .. .o .o oo .. o. .o o. .. o. .o .. .. .o o.
    .o .. o. o. o. .. o. o. .. o. .. o. .. .. .. o. o. .. o.
    >>> print_ostring(paragraph_to_braille('123'))
    .o o. .o o. .o oo
    .o .. .o o. .o ..
    oo .. oo .. oo ..
    >>> print_ostring(paragraph_to_braille('hElL0!'))
    o. .o o. o. .o o. .o .o ..
    oo .. .o o. .. o. .o oo oo
    .. .o .. o. .o o. oo .. o.
    >>> print_ostring(paragraph_to_braille('CHAT et Chien'))
    .o .o oo o. o. .o .. o. .o .. .o oo o. .o o. oo
    .. .. .. oo .. oo .. .o oo .. .. .. oo o. .o .o
    .o .o .. .. .. o. .. .. o. .. .o .. .. .. .. o.
    '''
    s = ''
    words = paragraph.split(' ')
    for i, word in enumerate(words):
        s += word_to_braille(word)
        if i != len(words) - 1:
            s += word_to_braille(' ')
    return s


######################################



def new_filename(fname, addition):
    '''(str) -> str
    Given a filename in format 'file.txt', add "_" then addition between
    the file name and extension.

    >>> new_filename("de_beauvoir.txt", "braille")
    'de_beauvoir_braille.txt'
    >>> new_filename("yo/README.csv", "braille")
    'yo/README_braille.csv'
    '''
    filename = fname[:-4] # to save its filename
    extension = fname[-4:] # to save its extension
    middlename = "_"+addition # save "_addition" as another string
    return filename+middlename+extension

    
def text_to_braille(text):
    '''(str) -> str
    Convert text to French Braille and return it as a Unicode string.
    >>> text_to_braille("Bonjour!")
    '⠨⠃⠕⠝⠚⠕⠥⠗⠖'
    >>> text_to_braille("Je m'appelle Élizabeth.")
    '⠨⠚⠑ ⠍⠄⠁⠏⠏⠑⠇⠇⠑ ⠨⠿⠇⠊⠵⠁⠃⠑⠞⠓⠲'
    >>> text_to_braille("COMP 202")
    '⠨⠨⠉⠕⠍⠏ ⠼⠃⠼⠚⠼⠃'
    >>> text_to_braille("COMP202")
    '⠨⠉⠨⠕⠨⠍⠨⠏⠼⠃⠼⠚⠼⠃'
    '''
    # handle newlines for students
    paragraphs = text.split('\n')
    total = ''
    for i, para in enumerate(paragraphs):
        big_ostring = paragraph_to_braille(para)
        big_unicode = paragraph_to_unicode(big_ostring)
        total += big_unicode

        if i < len(paragraphs) - 1: # keep paragraphs separate but no extra \ns
            total += '\n'

    return total


def file_read_platform_indep(fname):
    '''(str) -> str
    Read file and discard newlines so as to be platform independent,
    because Linux uses \\n, Windows uses \\r, and Mac \\r\\n.
    Kind of disappointing that this was necessary in 2019. :(
    >>> file_read_platform_indep('tests/test4.txt')
    'Hello COMP 202, shall we test your English Braille translator? (Will it work?)'
    '''
    with open(fname, 'r', encoding='utf8') as f:
        f_contents = f.read()
        f_contents = f_contents.replace('\n', '').replace('\r', '')
    return f_contents


def file_diff(fname1, fname2):
    '''(str, str) -> bool
    Compare the files named fname1 and fname2 line by line in a platform-independent
    fashion. Return if they are the "same".
    If they are not the same, output the diff.
    Sameness allows for an extra newline in the end of one of the two.

    >>> file_diff('tests/test4.txt', 'tests/test4.txt')
    True
    >>> file_diff('tests/expected6.txt', 'tests/expected6.txt')
    True
    >>> file_diff('tests/test4.txt', 'tests/expected4.txt')
    The files have different lengths.
    First different word: Hello
    Expected:             ⠠⠓⠑⠇⠇⠕
    False
    >>> file_diff('tests/test5.txt', 'tests/expected5.txt')
    The files have different lengths.
    First different word: English
    Expected:             ⠠⠑⠝⠛⠇⠊⠩
    False
    >>> file_diff('tests/test5.txt', 'tests/test6.txt')
    The files have different lengths.
    First different word: English
    Expected:             The
    False
    >>> file_diff('tests/expected1.txt', 'tests/expected2.txt')
    The files have different lengths.
    First different word: ⠨⠥⠝
    Expected:             ⠨⠑⠝
    False
    '''
    f_contents = file_read_platform_indep(fname1)
    g_contents = file_read_platform_indep(fname2)

    if f_contents == g_contents:
        return True

    # else return why different
    if len(f_contents) != len(g_contents):
        print('The files have different lengths.')

    f_words = f_contents.split(' ')
    g_words = g_contents.split(' ')
    for i, f_w in enumerate(f_words):
        if i < len(g_words):
            if f_words[i] != g_words[i]:
                print('First different word:', f_words[i])
                print('Expected:            ', g_words[i])
                return False    
    return False
   

def file_to_braille(fname, translation_function = text_to_braille, addition = "braille"):
    '''(str) -> NoneType
    Given French text in a file with name fname in folder tests/,
    convert it into French Braille in Unicode.
    Save the result to fname + "_braille".

    >>> file_to_braille('test1.txt')
    >>> file_diff('tests/test1_braille.txt', 'tests/expected1.txt')
    True
    >>> file_to_braille('test2.txt')
    >>> file_diff('tests/test2_braille.txt', 'tests/expected2.txt')
    True
    >>> file_to_braille('test3.txt')
    >>> file_diff('tests/test3_braille.txt', 'tests/expected3.txt')
    True
    '''    
    direc = 'tests/'
    with open(direc + fname, 'r', encoding='utf8') as f:
        text = f.read()

    output_file = new_filename(fname, addition)
    with open(direc + output_file, 'w+', encoding='utf8') as g:
        translation = translation_function(text)    
        print(translation, file = g)


if __name__ == '__main__':
    doctest.testmod()

