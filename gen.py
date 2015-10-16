#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Honeyword generation.')
parser.add_argument('-n', dest='number', type=int, default=9,
                    help=('total number of sweetwords to '
                          'generate (inclusive of P)'))
parser.add_argument('password', nargs='+', type=str, help='true password(s)')
args = parser.parse_args()


def main():
    print("Arguments: %s" % (args))
    print('TODO: everything')


if __name__ == '__main__':
    main()
