#!/usr/bin/env python

import sys
import csv
from genword import generate_word

ROCKYOU_100_FILENAME = 'rockyou-withcount-100.txt'
ROCKYOU_FULL_FILENAME = 'rockyou-withcount.txt'


def generate_sweetwords1(num, password):
    return [password for i in range(num)]


def generate_sweetwords2(num, password):
    # read rockyou_100
    # do something
    # generate sweetwords
    return [password for i in range(num)]


def generate_sweetwords3(num, password):
    return [password for i in range(num)]


def generate_sweetword_sets(num, passwords, sweetfunc):
    return [sweetfunc(num, p.strip()) for p in passwords]


def write_sweetwords(csv_writer, sweet_sets, newlines=2):
    for sweet_set in sweet_sets:
        csv_writer.writerow(sweet_set)
    for i in range(newlines):
        csv_writer.writerow('')


def main():
    num = int(sys.argv[1])
    in_filename = sys.argv[2]
    out_filename = sys.argv[3]

    with open(in_filename, 'r') as infile:
        passwords = infile.readlines()

    print('---- Sweetwords Generator ----')
    print('Reading passwords from %s\nWriting %d sweetwords/password to %s' % (
           in_filename, num, out_filename))

    with open(out_filename, 'wb') as outfile:
        sweet_writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_NONE)

        sweet1 = generate_sweetword_sets(num, passwords, generate_sweetwords1)
        write_sweetwords(sweet_writer, sweet1)

        sweet2 = generate_sweetword_sets(num, passwords, generate_sweetwords2)
        write_sweetwords(sweet_writer, sweet2)

        sweet3 = generate_sweetword_sets(num, passwords, generate_sweetwords3)
        write_sweetwords(sweet_writer, sweet3, newlines=0)

        # write_sweetwords(sweet1)
        # for sweetword_set in sweet1:
        #     sweet_writer.writerow(sweetword_set)


        # sweet_writer.writerow('')
        # sweet_writer.writerow('')

        # for sweetword_set in sweet2:
        #     sweet_writer.writerow(sweetword_set)
        # sweet_writer.writerow('')
        # sweet_writer.writerow('')


        # for sweetword_set in sweet3:
        #     sweet_writer.writerow(sweetword_set)

    print('Finished outputting sweetwords')


if __name__ == '__main__':
    try:
        main()
    except IndexError:
        print('Error parsing command line arguments, %s' % sys.argv[1:])
        sys.exit(1)
    except IOError:
        print('Error opening input file, %s' % sys.argv[1:])
        sys.exit(1)
