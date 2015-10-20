#!/usr/bin/env python2

import string
from random import random, randrange, choice


VOWELS = 'aeiou'
LETTERS = string.ascii_lowercase
CONSONANTS = string.join([c for c in string.ascii_lowercase
                          if c not in VOWELS], '')
# h, j, k, q, w, x, y are rarely doubled
DOUBLE_CONSONANTS = [c + c for c in CONSONANTS if c not in 'hjkqwxy']


# http://www.readingrockets.org/article/six-syllable-types
def closed_syllable():
    return choice(CONSONANTS) + choice(VOWELS) + choice(CONSONANTS)


def open_syllable():
    return choice(CONSONANTS) + choice(VOWELS)


def vce_syllable():
    r = random()
    v = ''
    if r < 0.95:
        v = choice([c for c in VOWELS if c != 'e'])
    else:
        v = choice(VOWELS)
    return v + choice(CONSONANTS) + 'e'


def vowel_team_syllable():
    r = random()
    if r < 0.30:
        return choice(['oo', 'ee'])
    if r < 0.70:
        v = choice(VOWELS)
        return v + choice([c for c in VOWELS if c != v])
    if r < 0.80:
        return choice(['ey', 'ay', 'oy', 'uy'])
    if r < 0.90:
        return choice(['ew', 'aw', 'ow'])
    # e.g. apprecia*tion*
    return (choice(CONSONANTS) + choice(VOWELS) + choice(VOWELS) +
            choice(CONSONANTS))


def vowel_r_syllable():
    r = random()
    if r < 0.50:
        return choice(CONSONANTS) + choice(VOWELS) + 'r'
    return choice(VOWELS) + 'r'


def c_le_syllable():
    return choice(CONSONANTS) + 'le'


def generate_syllable():
    c = ''
    r = random()
    if r > 0.80:
        c += choice(CONSONANTS)

    return c + choice([
        closed_syllable,
        open_syllable,
        vce_syllable,
        vowel_team_syllable,
        vowel_r_syllable,
        c_le_syllable
    ])()


def generate_syllable_num():
    r = random()
    if r < 0.05:
        return 1
    if r < 0.65:
        return 2
    if r < 0.90:
        return 3
    if r < 0.95:
        return 4
    if r < 0.98:
        return 5
    return 6


def generate_word():
    word = ''
    num_syllables = generate_syllable_num()

    for i in range(num_syllables):
        word += generate_syllable()

    while len(word) < 4:
        word += generate_syllable()

    return word


def equal_char_replace(some_str):

    for i in range(len(some_str)):
        # This is the current character at index i, and the left and right substrings
        some_str_loc = some_str[i:i+1]
        some_str_left = some_str[:i]
        some_str_right = some_str[i+1:]

        # If the letter is any of the ones listed replace with new character with a predefined probability
        if('A' in some_str_loc):
            if(random() < 0.20):
                some_str = some_str_left+str('4')+some_str_right
        if('a' in some_str_loc):
            if(random() < 0.10):
                some_str = some_str_left+str('@')+some_str_right
        if('o' in some_str_loc):
            if(random() < 0.60):
                some_str = some_str_left+str('0')+some_str_right
        if('e' in some_str_loc):
            if(random() < 0.30):
                some_str = some_str_left+str('3')+some_str_right
        if('l' in some_str_loc):
            if(random() < 0.25):
                some_str = some_str_left+str('l')+some_str_right
        if('s' in some_str_loc):
            if(random() < 0.25):
                some_str = some_str_left+str('$')+some_str_right
        if('T' in some_str_loc):
            if(random() < 0.15):
                some_str = some_str_left+str('7')+some_str_right
    return some_str


def can_capitalize(str):
    return any(c.isalpha() for c in str)


def tweak_capitalize(str):
    # generate a random number from 0 to 1
    pick = random.random()
    n = random.randint(0, len(str))
    # print pick, n
    if pick < .3:
        # print "proper"
        return str.title()
    elif pick < .5:
        # print "upper"
        return str.upper()
    elif pick < .8:
        # print "lower"
        return str.lower()
    else:
        s = ''
        for i in range(len(str)):
            j = random.random()
            if j > .65:
                s += (str[i].upper())
            else:
                s += (str[i].lower())
        return s


def can_addvowel(str):
    countVowels = 0
    for c in str:
        if c in VOWELS:
            countVowels += 1
    return countVowels > 0


def tweak_addvowel(str):
    s = ''
    for c in str:
        if c in VOWELS:
            for i in range(random.randint(1, 4)):
                s += c
        else:
            s += c
    return s


def can_pluralize(str):
    return any(c.isalpha() for c in str)


def tweak_pluralize(str):
    alpha = []
    numbers = []
    for i in range(len(str)):
        if str[(i+1)*-1].isalpha():
            alpha.append(len(str)+(i+1)*-1)

    if str[alpha[0]] == 's':
        s = str[0:alpha[0]] + str[alpha[0]+1:len(str)]
    else:
        s = str[0:alpha[0]+1] + 's' + str[alpha[0]+1:len(str)]
    return s


def main():
    for i in range(10):
        genword = generate_word()
        print genword

if __name__ == '__main__':
    main()
