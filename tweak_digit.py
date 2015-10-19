import re
import random
import string

def can_digit_tweak(str):
  for c in str:
    if c in '1234567890':
      return True
  return False

DIGITS = '0123456789'
def digit_tweak(password):
    new_password = [c for c in password]
    for i, c in enumerate(new_password):
        if c in DIGITS:
            new_password[i] = DIGITS[random.randrange(len(DIGITS))]
    return string.join(new_password, '')

samples = ['qwerty', 'password1', '123456', 'pass1word']
for sample in samples:
    if can_digit_tweak(sample):
        print('`%s` --> `%s`' % (sample, digit_tweak(sample)))
    else:
        print('Cannot digit tweak password `%s`' % sample)