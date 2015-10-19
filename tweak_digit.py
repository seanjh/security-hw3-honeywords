import re

def can_digit_tweak(str):
  for c in str:
    if c in '1234567890':
      return True
  return False


DIGIT_REGEX = re.compile(r'[0-9]{1}')
def digit_tweak(password):
    for match in DIGIT_REGEX.finditer(password):
        print 'Matched %s at %s' % (match.string, match.pos)
    return password

# assert can_digit_tweak('hello123'), False
# assert can_digit_tweak('124'), True
print digit_tweak('hello123')
print digit_tweak('1234')


def tweak(mystr):
    if can_digit_tweak(mystr):
        new_pass = digit_tweak(mystr)