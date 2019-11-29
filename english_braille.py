# Part 5
# Author: Yian Bian 260886212

from text_to_braille import *

ENG_CAPITAL = '..\n..\n.o'
end_number = '..\n.o\n.o'

####################################################
def two_letter_contractions(text):
    '''(str) -> str
    Process English text so that the two-letter contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.
    >>> two_letter_contractions('chat')
    'âat'
    >>> two_letter_contractions('shed')
    'îë'
    >>> two_letter_contractions('shied')
    'îië'
    >>> two_letter_contractions('showed the neighbourhood where')
    'îœë ôe neiêbürhood ûïe'
    >>> two_letter_contractions('SHED')
    'ÎË'
    >>> two_letter_contractions('ShOwEd tHE NEIGHBOURHOOD Where') 
    'ÎŒË tHE NEIÊBÜRHOOD Ûïe'
    '''
    combos = ['ch', 'gh', 'sh', 'th', 'wh', 'ed', 'er', 'ou', 'ow']
    for i, c in enumerate(combos):
        text = text.replace(c, LETTERS[-1][i])
    for i, c in enumerate(combos):
        text = text.replace(c.upper(), LETTERS[-1][i].upper())
    for i, c in enumerate(combos):
        text = text.replace(c.capitalize(), LETTERS[-1][i].upper())

    return text


def whole_word_contractions(text):
    '''(str) -> str
    Process English text so that the full-word contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    If the full-word contraction appears within a word, 
    contract it. (e.g. 'and' in 'sand')

    >>> whole_word_contractions('with')
    'ù'
    >>> whole_word_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meow'
    >>> whole_word_contractions('With')
    'Ù'
    >>> whole_word_contractions('WITH')
    'Ù'
    >>> whole_word_contractions('wiTH')
    'wiTH'
    >>> whole_word_contractions('FOR thE Cat WITh THE purr And The meow')
    'É thE Cat WITh À purr Ç À meow'
    >>> whole_word_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> whole_word_contractions('wither')
    'ùer'
    '''
    # putting 'with' first so wither becomes with-er not wi-the-r
    words = ['with', 'and', 'for', 'the']
    fr_equivs = ['ù', 'ç', 'é', 'à', ]
    # lower case
    for i, w in enumerate(words):
        text = text.replace(w, fr_equivs[i])
    for i, w in enumerate(words):
        text = text.replace(w.upper(), fr_equivs[i].upper())
    for i, w in enumerate(words):
        text = text.replace(w.capitalize(), fr_equivs[i].upper())
    return text



####################################################
def convert_contractions(text):
    '''(str) -> str
    Convert English text so that both whole-word contractions
    and two-letter contractions are changed to the appropriate
    French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    >>> convert_contractions('with')
    'ù'
    >>> convert_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meœ'
    >>> convert_contractions('chat')
    'âat'
    >>> convert_contractions('wither')
    'ùï'
    >>> convert_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> convert_contractions('Showed The Neighbourhood Where')
    'Îœë À Neiêbürhood Ûïe'
    '''
    # change whole-word contractions and two-letter contractions
    # to appropriate French accented letter
    text = whole_word_contractions(text)
    text = two_letter_contractions(text)
    return text


def convert_quotes(text):
    '''(str) -> str
    Convert the straight quotation mark into open/close quotations.
    >>> convert_quotes('"Hello"')
    '“Hello”'
    >>> convert_quotes('"Hi" and "Hello"')
    '“Hi” and “Hello”'
    >>> convert_quotes('"')
    '“'
    >>> convert_quotes('"""')
    '“”“'
    >>> convert_quotes('" "o" "i" "')
    '“ ”o“ ”i“ ”'
    '''
    num = 0 # to count the occurence of '"'
    for i in range(len(text)):
        if text[i] == '"' and num % 2 == 0:
        # because we first have'“',so ’"' should be '“' when number is even
        
        # so change '"' into '“' when num is even number
            text = text[:i] + "“"+ text[i+1:]
            num += 1
        elif text[i] == '"' and num % 2 == 1:
        # because we have'”' after we have'“',so ’"' should be '”' when number is odd
        
        # so change '"' into '”' when num is odd number
            text = text[:i] + "”" + text[i+1:]
            num += 1

    return text


####################################################
# Put your own helper functions here!

def is_not_digit(i):
    """
    (str) -> bool
    Return whether character c represents a single non_digit character.
    >>> is_not_digit('c')
    True
    >>> is_not_digit('G')
    True
    >>> is_not_digit('Hi')
    False
    >>> is_not_digit('0')
    False
    >>> is_not_digit('12')
    False
    """
    # to see if it's a single digit
    if is_digit(i) or len(i) != 1:
        return False
    else:
        return True

def track_begin_number(text):
    """
    (str) -> str
    add "先" to the front of every beginning digit
    >>> track_begin_number('2')
    '先2'
    >>> track_begin_number('COMP 202')
    'COMP 先202'
    >>> track_begin_number('COMP 202 AND COMP 250')
    'COMP 先202 AND COMP 先250'
    """
    i = 1
    text = "a"+text+"a" # add to letters to avoid IndexError
    while i <= len(text)-1:
        if is_digit(text[i]) and is_not_digit(text[i-1]):# to see if text[i] is the first digit
            text = text[:i]+"先"+text[i:] # if it is ,then use 先 to track the first digit
            # use 先 to track because it's a chinese, it won't appear in the english text
            i += 2 # because we add 先 to the string, we need to add 2 to i to skip 先
        else:
            i += 1 # we don't find the first digit in this iteration, so just add 1 
    text = text[1:(len(text)-1)] # to remove the 2 letters that we add in the beginning
    return text

def track_last_number(text):
    """
    (str) -> str
    add "后" to the front of every beginning digit
    >>> track_last_number('2')
    '2后'
    >>> track_last_number('COMP 202')
    'COMP 202后'
    >>> track_last_number('COMP 202 AND COMP 250')
    'COMP 202后 AND COMP 250后'
    """
    i = 1
    text = "a"+text+"a" # add to letters to avoid IndexError
    while i <= len(text)-1:
        if is_digit(text[i]) and is_not_digit(text[i+1]):# to see if text[i] is the last digit
            text = text[:(i+1)]+"后"+text[(i+1):]# if it is ,then use 后 to track the last digit
            # use 后 to track because it's a chinese, it won't appear in the english text
            i += 2 # because we add 后 to the string, we need to add 2 to i to skip 后
        else:
            i += 1 #  the digits still continue we don't find the last digit in this iteration, so just add 1
    text = text[1:(len(text)-1)] # to remove the 2 letters that we add in the beginning
    return text
   
   

def replace_number(text):
    """
    (int) -> str
    replace number with the letter that have the same braille
    >>> replace_number("COMP 202")
    'COMP bjb'
    >>> replace_number("2")
    'b'
    >>> replace_number("COMP 202 AND COMP 250")
    'COMP bjb AND COMP bej'
    """
    # if we convert digits directly, they will have ⠼ in between them.
    # so we use the letter which have the same braille to replace them 
    text = text.replace("1","a")
    text = text.replace("2","b")
    text = text.replace("3","c")
    text = text.replace("4","d")
    text = text.replace("5","e")
    text = text.replace("6","f")
    text = text.replace("7","g")
    text = text.replace("8","h")
    text = text.replace("9","i")
    text = text.replace("0","j")
    return text

    
def convert_punctuation(text):
    """
    (str) -> str
    replace the punctuation with the one that have the right braille in english braille
    >>> convert_punctuation("(hi)")
    '"hi"'
    >>> convert_punctuation('"hi"')
    '(hi)'
    >>> convert_punctuation("hi?")
    'hi('
    """
    text = convert_quotes(text) # first convert '""' into'“”'
    # because '(' and ')' have the same braille
    # so we first replace them with '#'
    text = text.replace("(","#")
    text = text.replace(")","#")
    # then replace'#' with'"' which has the braille for both '('and')'
    text = text.replace("#",'"')
    # braille for '“'in english is the same as'(' in french
    # so we replace'“' with '('
    # the same with '”' and ')'
    text = text.replace("“","(")
    text = text.replace("”",")")
    # braille for '?'in english is the same as'(' in french
    # so we replace'?' with '('
    text = text.replace("?","(")
    return text

####################################################

def english_text_to_braille(text):
    '''(str) -> str
    Convert text to English Braille. Text could contain new lines.

    >>> english_text_to_braille('202') # numbers
    '⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('2') # single digit
    '⠼⠃⠰'
    >>> english_text_to_braille('COMP') # all caps
    '⠠⠠⠉⠕⠍⠏'
    >>> english_text_to_braille('COMP 202') # combining number + all caps
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('and')
    '⠯'
    >>> english_text_to_braille('and And AND aNd')
    '⠯ ⠠⠯ ⠠⠯ ⠁⠠⠝⠙'
    >>> english_text_to_braille('chat that the with')
    '⠡⠁⠞ ⠹⠁⠞ ⠷ ⠾'
    >>> english_text_to_braille('hi?')
    '⠓⠊⠦'
    >>> english_text_to_braille('(hi)')
    '⠶⠓⠊⠶'
    >>> english_text_to_braille('"hi"')
    '⠦⠓⠊⠴'
    >>> english_text_to_braille('COMP 202 AND COMP 250')
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰ ⠠⠯ ⠠⠠⠉⠕⠍⠏ ⠼⠃⠑⠚⠰'
    >>> english_text_to_braille('For shapes with colour?')
    '⠠⠿ ⠩⠁⠏⠑⠎ ⠾ ⠉⠕⠇⠳⠗⠦'
    >>> english_text_to_braille('(Parenthetical)\\n\\n"Quotation"')
    '⠶⠠⠏⠁⠗⠑⠝⠷⠞⠊⠉⠁⠇⠶\\n\\n⠦⠠⠟⠥⠕⠞⠁⠞⠊⠕⠝⠴'
    >>> english_text_to_braille('... and, word.')
    '⠲⠲⠲ ⠯⠂ ⠺⠕⠗⠙⠲'
    '''
    text = convert_contractions(text) # first change whole-word contractions and two-letter contractions
    # to appropriate French accented letter
    text = convert_punctuation(text) # then convert the punctuation
    text = track_begin_number(text) # track the first digit
    text = track_last_number(text) # track the last digit
    text = replace_number(text) # replace the number with corresponding letter
    text = text_to_braille(text) # convert the text to braille
    text = text.replace("先",ostring_to_unicode(".o\n.o\noo"))
    # replace the sign we use to track the first digit with ⠼, to show it's digit 
    text = text.replace("后",ostring_to_unicode("..\n.o\n.o"))
    # replace the sign we use to track the last digit with⠰ , to show it's the end of digit 
    text = text.replace(ostring_to_unicode(CAPITAL), ostring_to_unicode('..\n..\n.o'))
    # french braille and english braille have different way to show the capital letter
    # so we replace the french way with english way
    return text
    


def english_file_to_braille(fname):
    '''(str) -> NoneType
    Given English text in a file with name fname in folder tests/,
    convert it into English Braille in Unicode.
    Save the result to fname + "_eng_braille".
    >>> english_file_to_braille('test4.txt')
    >>> file_diff('tests/test4_eng_braille.txt', 'tests/expected4.txt')
    True
    >>> english_file_to_braille('test5.txt')
    >>> file_diff('tests/test5_eng_braille.txt', 'tests/expected5.txt')
    True
    >>> english_file_to_braille('test6.txt')
    >>> file_diff('tests/test6_eng_braille.txt', 'tests/expected6.txt')
    True
    '''  
    file_to_braille(fname, english_text_to_braille, "eng_braille")


if __name__ == '__main__':
    doctest.testmod()    # you may want to comment/uncomment along the way
    # and add tests down here
