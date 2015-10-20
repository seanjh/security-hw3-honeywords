#!/usr/bin/env python2

import string
import re
from random import random, randrange, choice

MAX_PASSWORD_LENGTH = 256
PASSWORD_PUNCTUATION = '!@#$%^&*+-<>?:;'
ALL_PASSWORD_CHARS = string.ascii_letters + string.digits + PASSWORD_PUNCTUATION
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


def tough_nut_length():
    r = random()
    if r < 0.05:
        return randrange(0, 5)
    if r < 0.45:
        return randrange(5, 10)
    if r < 0.90:
        return randrange(10, 40)
    if r < 0.95:
        return randrange(40, 100)
    return randrange(100, MAX_PASSWORD_LENGTH)


def generate_tough_nut():
    char_count = tough_nut_length()
    toughie = []
    for i in range(char_count):
        toughie.append(choice(ALL_PASSWORD_CHARS))
    return string.join(toughie, '')


def generate_seed(tough_nut_prob=0.08):
    r = random()
    if r < tough_nut_prob:
        return generate_tough_nut()
    return generate_word()


def can_equal_char_replace(password):
    return any([True for c in password if c in 'AELOSTaelost@310$7@310$7'])


def tweak_equal_char_replace(password):
    for i in range(len(password)):
        # This is the current character at index i, and the left and right
        # substrings
        password_loc = password[i:i+1]
        password_left = password[:i]
        password_right = password[i+1:]

        # If the letter is any of the ones listed replace with new character
        # with a predefined probability
        if('A' in password_loc):
            if(random() < 0.20):
                password = password_left+str('4')+password_right
        if('a' in password_loc):
            if(random() < 0.10):
                password = password_left+str('@')+password_right
        if('o' in password_loc):
            if(random() < 0.60):
                password = password_left+str('0')+password_right
        if('e' in password_loc):
            if(random() < 0.30):
                password = password_left+str('3')+password_right
        if('l' in password_loc):
            if(random() < 0.25):
                password = password_left+str('l')+password_right
        if('s' in password_loc):
            if(random() < 0.25):
                password = password_left+str('$')+password_right
        if('T' in password_loc):
            if(random() < 0.15):
                password = password_left+str('7')+password_right
    return password


def can_capitalize(password):
    return any(c.isalpha() for c in password)


def tweak_capitalize(password):
    # generate a random number from 0 to 1
    pick = random()
    n = randrange(0, len(password))
    # print pick, n
    if pick < .3:
        # print "proper"
        return password.title()
    elif pick < .5:
        # print "upper"
        return password.upper()
    elif pick < .8:
        # print "lower"
        return password.lower()
    else:
        s = ''
        for i in range(len(password)):
            j = random()
            if j > .65:
                s += (password[i].upper())
            else:
                s += (password[i].lower())
        return s


def can_add_vowel(password):
    countVowels = 0
    for c in password:
        if c in VOWELS:
            countVowels += 1
    return countVowels > 0


def tweak_add_vowel(password):
    s = ''
    for c in password:
        if c in VOWELS:
            for i in range(randrange(1, 4)):
                s += c
        else:
            s += c
    return s


def can_pluralize(password):
    return any(c.isalpha() for c in password)


def tweak_pluralize(password):
    alpha = []
    numbers = []
    for i in range(len(password)):
        if password[(i+1)*-1].isalpha():
            alpha.append(len(password)+(i+1)*-1)

    if password[alpha[0]] == 's':
        new_str = password[0:alpha[0]] + password[alpha[0] + 1:len(password)]
    else:
        new_str = (password[0:alpha[0]+1] +
                   's' + password[alpha[0] + 1:len(password)])
    return new_str


def can_digit_tweak(password):
    return any([True for c in password if c in string.digits])


def tweak_digits(password):
    new_password = [c for c in password]
    for i, c in enumerate(new_password):
        if c in string.digits:
            new_password[i] = string.digits[randrange(len(string.digits))]
    return string.join(new_password, '')


def can_tweak_tail(password):
    return True


def tweak_tail(password):
    tweak_chars = randrange(1, len(password))
    new_password = [c for c in password]
    for i in range(tweak_chars, -1, -1):
        pos = len(password) - 1 - i
        c = new_password[pos]
        if c in string.ascii_lowercase:
            new_password[pos] = choice(string.ascii_lowercase)
        elif c in string.ascii_uppercase:
            new_password[pos] = choice(string.ascii_uppercase)
        elif c in string.digits:
            new_password[pos] = choice(string.digits)
        elif c in PASSWORD_PUNCTUATION:
            new_password[pos] = choice(PASSWORD_PUNCTUATION)
        else:
            new_password[pos] = choice(string.ascii_letters)

    return string.join(new_password, '')


def select_tweak_func(password):
    funcs = []
    if can_digit_tweak(password):
        funcs.append(tweak_digits)
    if can_pluralize(password):
        funcs.append(tweak_pluralize)
    if can_add_vowel(password):
        funcs.append(tweak_add_vowel)
    if can_capitalize(password):
        funcs.append(tweak_capitalize)
    if can_equal_char_replace(password):
        funcs.append(tweak_equal_char_replace)
    assert(len(funcs) > 0)
    return choice(funcs)


def test_tweak_funcs(password):
    if can_digit_tweak(password):
        print('tweak_digits: %s-->%s' % (password, tweak_digits(password)))
    else:
        print('Cannot apply %s to %s' % ('tweak_digits', password))
    if can_pluralize(password):
        print('tweak_pluralize: %s-->%s' % (password, tweak_pluralize(password)))
    else:
        print('Cannot apply %s to %s' % ('tweak_pluralize', password))
    if can_add_vowel(password):
        print('tweak_add_vowel: %s-->%s' % (password, tweak_add_vowel(password)))
    else:
        print('Cannot apply %s to %s' % ('tweak_add_vowel', password))
    if can_capitalize(password):
        print('tweak_capitalize: %s-->%s' % (password, tweak_capitalize(password)))
    else:
        print('Cannot apply %s to %s' % ('tweak_capitalize', password))
    if can_equal_char_replace(password):
        print('tweak_equal_char_replace: %s-->%s' % (password, tweak_equal_char_replace(password)))
    else:
        print('Cannot apply %s to %s' % ('tweak_equal_char_replace', password))
    if can_tweak_tail(password):
        print('tweak_tail: %s-->%s' % (password, tweak_tail(password)))
    else:
        print('Cannot apply %s to %s' % ('tweak_tail', password))


def main():
    for i in range(100):
        seed = generate_seed()
        print('New seed: %s' % seed)
        test_tweak_funcs(seed)
        print

if __name__ == '__main__':
    main()
