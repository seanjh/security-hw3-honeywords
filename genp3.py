#!/usr/bin/env python2

import string
import random
from genword import (generate_word, generate_tough_nut, TOUGH_NUT_PROBABILITY,
                     RANDOM_WORD_PROBABILITY)
from sweetwordutils import (parse_args, load_input, write_sweetwords,
                            mod_count, generate_seeds, generate_tweaks,
                            load_rockyou_passwords, choose_rockyou)

ROCKYOU_FULL_FILENAME = 'rockyou-withcount.txt'
PROBLEM_NUM = 3


def generate_sweetwords(num_sweetwords, known_passwords, pass_weights,
                        real_password, random_word_prob=RANDOM_WORD_PROBABILITY,
                        tough_nut_prob=TOUGH_NUT_PROBABILITY):
    sweetwords = [real_password]  # initiate the honeywords with the sweetwords

    num_seeds = mod_count(num_sweetwords)
    while len(sweetwords) < num_seeds:
        r = random.random()
        # generate a new word using 1 of 3 methods
        if (r < tough_nut_prob):
            new_word = generate_tough_nut()
        if r < random_word_prob:
            new_word = generate_word()
        else:
            new_word = choose_rockyou(known_passwords, pass_weights, num=1)[0]

        if new_word not in sweetwords:
            # add the generated word
            sweetwords.append(new_word)

    # sweetwords with sqrt(n)-1 elements+password
    tweaks = generate_tweaks(num_sweetwords, sweetwords)
    random.shuffle(tweaks)
    return tweaks


def generate_sweetword_sets(num_sweetwords, real_passwords, known_passwords,
                            pass_weights):
    return [generate_sweetwords(num_sweetwords, known_passwords, pass_weights,
                                p.strip())
            for p in real_passwords]


def main():
    num_sweetwords, in_filename, out_filename = parse_args()
    real_passwords = load_input(in_filename)

    print('---- Sweetwords Generator Problem #%s ----' % PROBLEM_NUM)
    print('Reading passwords from %s\nWriting %d sweetwords/password to %s' % (
           in_filename, num_sweetwords, out_filename))

    known_pass_counts, known_pass_weights, known_passwords, total_count = (
        load_rockyou_passwords())

    sweets = generate_sweetword_sets(num_sweetwords, real_passwords,
                                     known_passwords, known_pass_weights)
    write_sweetwords(out_filename, sweets)

    print('---- Finished Sweetwords Generator Problem #%d ----' % PROBLEM_NUM)


if __name__ == '__main__':
    main()
