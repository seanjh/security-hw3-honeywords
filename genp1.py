#!/usr/bin/env python

import random
from math import sqrt, ceil
from genword import generate_word
from sweetwordutils import (parse_args, load_input, write_sweetwords,
                            seed_tweaks_count, generate_seeds, generate_tweaks)

PROBLEM_NUM = 1


def generate_sweetwords(seed_count, tweak_count, password):
    seeds = generate_seeds(seed_count, password)

    sweetwords = []
    for seed in seeds:
        sweetwords += generate_tweaks(tweak_count, seed)
    random.shuffle(sweetwords)
    return sweetwords


def generate_sweetword_sets(num, passwords):
    count = seed_tweaks_count(num)
    return [generate_sweetwords(count, count, p.strip()) for p in passwords]


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
