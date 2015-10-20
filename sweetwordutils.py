import sys
import csv
import math
import random
from genword import generate_seed, select_tweak_func


def generate_sweetword_sets(num, passwords):
    count = seed_tweaks_count(num)
    return [generate_sweetwords(count, count, p.strip()) for p in passwords]


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


def seed_tweaks_count(num):
    return int(math.ceil(math.sqrt(num)))


def generate_seeds(num, password=None):
    seeds = []
    if password:
        seeds.append(password)
    seeds += [generate_seed() for i in range(num - 1 if password else num)]
    random.shuffle(seeds)
    return seeds


def generate_tweaks(num, seed):
    tweak_func = select_tweak_func(seed)
    return [tweak_func(seed) for i in range(num)]
