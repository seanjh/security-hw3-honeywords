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


def main():
    for i in range(10):
        print generate_word()


if __name__ == '__main__':
    main()
