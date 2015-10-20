#!/usr/bin/env python
import string
from genword import generate_word
from sweetwordutils import (parse_args, load_input, write_sweetwords,
                            mod_count, generate_seeds, generate_tweaks)
from genp3 import (db_count, generate_sweetwords, choose_rockyou,
                   generate_sweetword_sets, rock_you_db)

ROCKYOU_FULL_FILENAME = 'rockyou-withcount.txt'
PROBLEM_NUM = 2


def rock_you_db_1(most_common):
    rockyou = rock_you_db()
    rockyou_most_common = rockyou[:most_common]
    return rockyou_most_common


def main():
    num, in_filename, out_filename = parse_args()
    passwords = load_input(in_filename)
    print('---- Sweetwords Generator Problem #%s ----' % PROBLEM_NUM)
    print('Reading passwords from %s\nWriting %d sweetwords/password to %s' % (
           in_filename, num, out_filename))

    # 10 most common passwords from the rock you db
    rockyou_most_common = rock_you_db_1(100)

    sweets = generate_sweetword_sets(num, passwords, rockyou_most_common,
                                     db_count(rockyou_most_common))
    write_sweetwords(out_filename, sweets)

    print('---- Finished Sweetwords Generator Problem #%d ----' % PROBLEM_NUM)


if __name__ == '__main__':
    main()
