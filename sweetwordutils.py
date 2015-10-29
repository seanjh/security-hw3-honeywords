import sys
import csv
import math
import random
import string
import numpy as np
from genword import generate_seed, select_tweak_func, tweak_tail

ROCKYOU_FULL_FILENAME = 'rockyou-withcount.txt'

# Indices for the tuples parsed from each line of the rockyou-withcount file
USES_INDEX = 0
PASSWORD_INDEX = 1


def parse_args():
    return int(sys.argv[1]), sys.argv[2], sys.argv[3]


def load_input(in_filename):
    with open(in_filename, 'r') as infile:
        return infile.readlines()


def write_sweetwords(out_filename, sweet_sets):
    with open(out_filename, 'wb') as outfile:
        sweet_writer = csv.writer(outfile, delimiter=',',
                                  quoting=csv.QUOTE_NONE, quotechar='')
        for sweet_set in sweet_sets:
            sweet_writer.writerow(sweet_set)


def mod_count(num):
    return int(math.ceil(math.sqrt(num)))


def generate_seeds(num, password=None):
    seeds = []
    if password:
        seeds.append(password)
    seeds += [generate_seed() for i in range(num - 1 if password else num)]
    random.shuffle(seeds)
    return seeds


def is_tweak_unique(tweak, other_tweaks):
    return tweak not in other_tweaks


def generate_tweak(seed, tweaks):
    tweak_func = select_tweak_func(seed)
    tweak_tries = 0
    new_tweak = seed
    while(not is_tweak_unique(new_tweak, tweaks) and tweak_tries < 10):
        new_tweak = tweak_func(seed)
        tweak_tries += 1
    # Fall back on tail tweaking if the selected tweak algorithm cannot
    # produce a unique tweak after 10 tries
    while(not is_tweak_unique(new_tweak, tweaks)):
        new_tweak = tweak_tail(seed)
    tweaks.append(new_tweak)


def generate_tweaks(num, seeds):
    num_tweaks = mod_count(num)
    tweaks = list(seeds)
    for seed in seeds:
        for i in range(num_tweaks):
            if len(tweaks) == num:
                break
            generate_tweak(seed, tweaks)
    random.shuffle(tweaks)
    return tweaks


def load_rockyou_passwords(limit=None, filename=ROCKYOU_FULL_FILENAME):
    with open(ROCKYOU_FULL_FILENAME, 'r') as infile:
        rockyou = []
        for i, line in enumerate(infile):
            val = tuple(line.split())
            try:
                val[USES_INDEX]
                val[PASSWORD_INDEX]
                rockyou.append(val)
            except IndexError as e:
                # all spaces
                pass
            if limit and (i + 1) >= limit:
                break

    uses = np.array([password[USES_INDEX] for password in rockyou],
                    dtype=np.uint32)
    total_uses = uses.sum()
    passwords = [password[PASSWORD_INDEX] for password in rockyou]
    weights = np.array(uses, dtype=np.float32)
    weights /= total_uses
    return uses, weights, passwords, total_uses


def choose_rockyou(passwords, weights, num=1):
    return np.random.choice(passwords, num, p=weights)
