#!/usr/bin/env python

import string
import random
from genword import generate_word
from sweetwordutils import (parse_args, load_input, write_sweetwords,
                            mod_count, generate_seeds, generate_tweaks)

ROCKYOU_FULL_FILENAME = 'rockyou-withcount.txt'
PROBLEM_NUM = 3

#converts rock you db in to tuples
def rock_you_db():
    with open(ROCKYOU_FULL_FILENAME, 'r') as infile:
        rockyou = [tuple(string.split(line)) for line in infile.readlines()]
    return rockyou

def rock_you_db_count(rockyou):
    num_elements=0
    for i in rockyou:
        num_elements+= int(i[0])
    return num_elements

def generate_sweetwords(num, password,rockyou,num_elements):
    sweetwords = [password] #initiate the honeywords with the sweetwords

    while len (sweetwords) < mod_count(num):

        #generate a new word
        r = random.randint(0,num_elements)
        new_word = choose_rockyou(rockyou,r)
        if new_word not in sweetwords:
            sweetwords.append(new_word) #add the new word to the list of sweetwords

    tweaks = generate_tweaks(num,sweetwords) #sweetwords with sqrt(n)-1 elements+pswd

    random.shuffle(tweaks)

    return tweaks

#choose a random word from rock
def choose_rockyou(rockyou,r):
    sum = 0
    for i in rockyou:
        sum+= int(i[0])
        if(r<=sum):
            return i[1]
    return "ERROR"


def generate_sweetword_sets(num, passwords,rockyou,num_elements):
    return [generate_sweetwords(num, p.strip(),rockyou,num_elements) for p in passwords]



def main():
    num, in_filename, out_filename = parse_args()
    passwords = load_input(in_filename)

    print('---- Sweetwords Generator Problem #%s ----' % PROBLEM_NUM)
    print('Reading passwords from %s\nWriting %d sweetwords/password to %s' % (
           in_filename, num, out_filename))

    #converts rock you db in to tuples
    rockyou = rock_you_db()
    #counts numb of elements in rock you db
    num_elements = rock_you_db_count(rockyou)

    sweets = generate_sweetword_sets(num, passwords,rockyou,num_elements)
    write_sweetwords(out_filename, sweets)

    print('---- Finished Sweetwords Generator Problem #%d ----' % PROBLEM_NUM)


if __name__ == '__main__':
    main()
