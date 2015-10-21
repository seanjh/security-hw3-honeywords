#!/usr/bin/env python2
import string
from genword import generate_word, generate_tough_nut, RANDOM_WORD_PROBABILITY
from sweetwordutils import (parse_args, load_input, write_sweetwords,
                            mod_count, generate_seeds, generate_tweaks)
from genp3 import (db_count, generate_sweetwords, choose_rockyou,
                   rock_you_db)

ROCKYOU_FULL_FILENAME = 'rockyou-withcount.txt'
PROBLEM_NUM = 2
ROCKYOU_CUTOFF = 100


def generate_sweetword_sets(num, passwords, rockyou, num_elements):
    return [generate_sweetwords(num, p.strip(), rockyou, num_elements,
                                RANDOM_WORD_PROBABILITY)
            for p in passwords]


def rock_you_db(limit=None):
    with open(ROCKYOU_FULL_FILENAME, 'r') as infile:
        rockyou = []
        for i, line in enumerate(infile):
            rockyou.append(string.split(line))
            if limit and (i + 1) >= limit:
                break
    return rockyou


def main():
    num, in_filename, out_filename = parse_args()
    passwords = load_input(in_filename)
    print('---- Sweetwords Generator Problem #%s ----' % PROBLEM_NUM)
    print('Reading passwords from %s\nWriting %d sweetwords/password to %s' % (
           in_filename, num, out_filename))

    # 10 most common passwords from the rock you db
    rockyou_most_common = rock_you_db(ROCKYOU_CUTOFF)

    sweets = generate_sweetword_sets(num, passwords, rockyou_most_common,
                                     db_count(rockyou_most_common))
    write_sweetwords(out_filename, sweets)

    print('---- Finished Sweetwords Generator Problem #%d ----' % PROBLEM_NUM)


if __name__ == '__main__':
    main()
