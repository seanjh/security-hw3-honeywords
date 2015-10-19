import sys
import csv

def parse_args():
    return int(sys.argv[1]), sys.argv[2], sys.argv[3]


def load_input(in_filename):
    with open(in_filename, 'r') as infile:
        return infile.readlines()


def write_sweetwords(out_filename, sweet_sets):
    with open(out_filename, 'wb') as outfile:
        sweet_writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_NONE)
        for sweet_set in sweet_sets:
            sweet_writer.writerow(sweet_set)