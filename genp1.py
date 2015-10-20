#!/usr/bin/env python

import random
from math import sqrt, ceil
from sweetwordutils import (parse_args, load_input, write_sweetwords,
                            mod_count, generate_seeds, generate_tweaks,
                            select_tweak_func)

PROBLEM_NUM = 1


def generate_sweetwords(num, password):
    seed_count = mod_count(num)
    seeds = generate_seeds(seed_count, password)

    sweetwords = generate_tweaks(num, seeds)
    random.shuffle(sweetwords)
    return sweetwords


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
