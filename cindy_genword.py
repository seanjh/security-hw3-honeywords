
import random
testString = raw_input("Input your password:\n")

def can_capitalize(str):
	return any(c.isalpha() for c in str)

def tweak_capitalize(str):
	# generate a random number from 0 to 1
	pick = random.random() 
	n = random.randint(0,len(str))
	# print pick, n
	if pick < .3:
		# print "proper"
		return str.title()
	elif pick < .5:
		# print "upper"
		return str.upper()
	elif pick < .8:
		# print "lower"
		return str.lower()
	else:
		s = ''
		for i in range(len(str)):
			j = random.random()
			if j > .65:
				s += (str[i].upper())
			else:
				s += (str[i].lower())
		return s

if can_capitalize(testString):
	print tweak_capitalize(testString)

VOWELS = 'aeiou'

def can_addvowel(str):
	countVowels = 0
	for c in str:
		if c in VOWELS:
			countVowels += 1
	return countVowels > 0

def tweak_addvowel(str):
	s = ''
	for c in str:
		if c in VOWELS:
			for i in range(random.randint(1,4)):
				s += c
		else:
			s += c
	return s

print tweak_addvowel(testString)

def can_pluralize(str):
	return any(c.isalpha() for c in str)


def tweak_pluralize(str):
	alpha = []
	numbers = []
	for i in range(len(str)):
		if str[(i+1)*-1].isalpha():
			alpha.append(len(str)+(i+1)*-1)
	
	if str[alpha[0]] == 's':
		s = str[0:alpha[0]] + str[alpha[0]+1:len(str)]
	else: 
		s = str[0:alpha[0]+1] + 's' + str[alpha[0]+1:len(str)]
	return s

print tweak_pluralize(testString)
