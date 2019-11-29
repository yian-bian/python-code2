# Part 3
# Author: Yian Bian
# Student ID: 260886212

import doctest

def ostring_to_raisedpos(s):
    ''' (str) -> str
    Convert a braille letter represented by '##\n##\n##' o-string format
    to raised position format.
    Braille cell dot position numbers:
    1 .. 4
    2 .. 5
    3 .. 6
    7 .. 8 (optional)

    >>> ostring_to_raisedpos('..\\n..\\n..')
    ''
    >>> ostring_to_raisedpos('oo\\noo\\noo')
    '142536'
    >>> ostring_to_raisedpos('o.\\noo\\n..')
    '125'
    >>> ostring_to_raisedpos('o.\\noo\\n..\\n.o')
    '1258'
    '''
    res = ''
    inds = [1, 4, 2, 5, 3, 6, 7, 8]
    s = s.replace('\n', '')
    for i, c in enumerate(s):
        if c == 'o':
            res += str(inds[i])
    return res 


def raisedpos_to_binary(s):
    ''' (str) -> str
    Convert a string representing a braille character in raised-position
    representation  into the binary representation.
    >>> raisedpos_to_binary('')
    '00000000'
    >>> raisedpos_to_binary('142536')
    '11111100'
    >>> raisedpos_to_binary('14253678')
    '11111111'
    >>> raisedpos_to_binary('123')
    '11100000'
    >>> raisedpos_to_binary('125')
    '11001000'
    >>> raisedpos_to_binary('278')
    '01000011'
    '''
    binary = "" # set a variable
    for i in range(1,9): # make i can be 1 to 8
        if s.find(str(i)) != -1: # to see if there is digit‘i'in s 
            binary = binary+"1" # if there is, then put'1' at the same position
        else:
            binary = binary + "0"# if there is not, put '0'
    return binary
    

def binary_to_hex(s):
    '''(str) -> str
    Convert a Braille character represented by an 8-bit binary string
    to a string representing a hexadecimal number.
    The first braille letter has the hex value 2800. Every letter
    therafter comes after it.

    To get the hex number for a braille letter based on binary representation:
    1. reverse the string
    2. convert it from binary to hex
    3. add 2800 (in base 16)

    >>> binary_to_hex('00000000')
    '2800'
    >>> binary_to_hex('11111100')
    '283f'
    >>> binary_to_hex('11111111')
    '28ff'
    >>> binary_to_hex('11001000')
    '2813'
    '''
    reverse = ''# set a variable
    for item in s:
        reverse = item + reverse #reverse the string
    dec_num = int(reverse,base=2) # convert the binary number into decimaml number
    hex_num = hex(dec_num + int("2800",base = 16)) # add 2800(in base 16) and then convert the sum
    return hex_num[2::]# return the number without the first teo letters'ox'



def hex_to_unicode(n):
    '''(str) -> str
    Convert a braille character represented by a hexadecimal number
    into the appropriate unicode character.
    >>> hex_to_unicode('2800')
    '⠀'
    >>> hex_to_unicode('2813')
    '⠓'
    >>> hex_to_unicode('2888')
    '⢈'
    '''
    # source: https://stackoverflow.com/questions/49958062/how-to-print-unicode-like-uvariable-in-python-2-7
    return chr(int(str(n),16))


def is_ostring(s):
    '''(str) -> bool
    Is s formatted like an o-string? It can be 6-dot or 8-dot.
    >>> is_ostring('o.\\noo\\n..')
    True
    >>> is_ostring('o.\\noo\\n..\\noo')
    True
    >>> is_ostring('o.\\n00\\n..\\noo')
    False
    >>> is_ostring('o.\\noo')
    False
    >>> is_ostring('o.o\\no\\n..')
    False
    >>> is_ostring('o.\\noo\\n..\\noo\\noo')
    False
    >>> is_ostring('\\n')
    False
    >>> is_ostring('A')
    False
    '''
    number_of_o = s.count('o') # count the number of 'o'
    number_of_period = s.count('.') # count the number of '.'
    number_of_slash_n  = s.count('\n') # count the number of '\n'
    # first make sure there's only two(three) lines
    # then every line only have two characters
    # last there's only 'o' '.'in every line
    if s.count('\n') == 2 and (s[2:3]) == (s[5:6]) == '\n' and  number_of_o+number_of_period+number_of_slash_n== 8:
        return True
    elif s.count('\n') == 3 and (s[2:3])==(s[5:6])==(s[8:9])=='\n' and number_of_o+number_of_period+number_of_slash_n == 11:
        return True
    else:
        return False
        


def ostring_to_unicode(s):
    '''
    (str) -> str
    If s is a Braille cell in o-string format, convert it to unicode.
    Else return s.

    Remember from page 4 of the pdf:
    o-string -> raisedpos -> binary -> hex -> Unicode
    >>> ostring_to_unicode('o.\\noo\\n..')
    '⠓'
    >>> ostring_to_unicode('o.\\no.\\no.\\noo')
    '⣇'
    >>> ostring_to_unicode('oo\\noo\\noo\\noo')
    '⣿'
    >>> ostring_to_unicode('oo\\noo\\noo')
    '⠿'
    >>> ostring_to_unicode('..\\n..\\n..')
    '⠀'
    >>> ostring_to_unicode('a')
    'a'
    >>> ostring_to_unicode('\\n')
    '\\n'
    >>> ostring_to_unicode('o.\\no.\\n..\\n..')
    '⠃'
    '''
    if is_ostring(s) == True: # to see if it's an o-string
        raisedpos = ostring_to_raisedpos(s) # o-string -> raisedpos
        binary = raisedpos_to_binary(raisedpos) # raisepos ->binary
        hex_num = binary_to_hex(binary) # binary -> hex
        unicode = hex_to_unicode(hex_num) # hex -> unicode
        return unicode
    else:
        return s
    


if __name__ == '__main__':
    doctest.testmod()
