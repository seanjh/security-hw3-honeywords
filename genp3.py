#!/usr/bin/env python

from genword import generate_word
from sweetwordutils import (parse_args, load_input, write_sweetwords,
                            seed_tweaks_count, generate_seeds, generate_tweaks)

ROCKYOU_FULL_FILENAME = 'rockyou-withcount.txt'
PROBLEM_NUM = 3


def generate_sweetwords(num, password):
    return [password for i in range(num)]


def generate_sweetword_sets(num, passwords):
    return [generate_sweetwords(num, p.strip()) for p in passwords]


def main():
    num, in_filename, out_filename = parse_args()
    passwords = load_input(in_filename)

    print('---- Sweetwords Generator Problem #%s ----' % PROBLEM_NUM)
    print('Reading passwords from %s\nWriting %d sweetwords/password to %s' % (
           in_filename, num, out_filename))

    sweets = generate_sweetword_sets(num, passwords)
    write_sweetwords(out_filename, sweets)

    print('---- Finished Sweetwords Generator Problem #%d ----' % PROBLEM_NUM)


if __name__ == '__main__':
    main()
