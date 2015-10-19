import sys
import csv
import math
import random
from genword import generate_word


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
        sweet_writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_NONE)
        for sweet_set in sweet_sets:
            print('Sweet set: %s' % sweet_set)
            sweet_writer.writerow(sweet_set)


def seed_tweaks_count(num):
    return int(math.ceil(math.sqrt(num)))


def generate_seeds(num, password=None):
    seeds = []
    if password:
        seeds.append(password)
    seeds += [generate_word() for i in range(num - 1 if password else num)]
    random.shuffle(seeds)
    return seeds


def generate_tweaks(num, seed):
    return [seed for i in range(num)]
