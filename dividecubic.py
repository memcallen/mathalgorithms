#!/usr/bin/python

import sys
import math

if len(sys.argv) != 7:
	print "Usage: python dividecubic.py a b c d a1 b1 where (ax^3 + bx^2 + cx + d) / (a1x - b1)"

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = int(sys.argv[4])

a1 = int(sys.argv[5])
b1 = int(sys.argv[6])

_a = a
_b = _a * (b1/a1) + b
_c = _b * (b1/a1) + c
_d = _c * (b1/a1) + d

print "Synthetic division: {0}, {1}, {2}, {3}".format(_a, _b, _c, _d)

print "Quadratic: {0}x^2 + {1}x + {2}".format(_a, _b, _c)


def stop(a, c, i):
	if abs(a * c) > 1000:
		return abs (a * c) / i > 2
	else:
		return 1

a = _a
b = _b
c = _c

factors = []

highest = 0

for i in range(1, abs(c * a) + 1):
	if abs(c * a) % i == 0 and stop(a, c, i):
		factors.append(i)
		factors.append(-i)
print "Factors of {0} (a*c) : {1}".format(c * a, factors)

zero = 0
zero2 = 0
found = 1

for x in factors:
	for y in factors:
		if x + y == b and x * y == a * c:
			print "Found Quadratic pair {0} + {1} = {2} & {0} * {1} = {3} * {4}".format(x, y, b, a, c).replace("+ -", "- ")
			zero = x
			zero2 = y
			found = 0

t1 = ""
t2 = ""

remainder = ""

if _d != 0:
	remainder = " + {2}/({0}x + {1})".format(a1, b1, _d).replace(" + -", " -")

if a != 1:
	if math.floor(zero / a + 0.5) == float(zero) / float(a):
		t1 = a
		print "Zero #2 - {0} / {1} = {2}".format(zero, a, zero / a)
		zero = zero / a
	elif math.floor(zero2 / a + 0.5) == float(zero2) / float(a):
		t1 = a
		print "Zero #2 - {0} / {1} = {2}".format(zero2, a, zero2 / a)
		zero2 = zero2 / a
	else:
		zero = "{0}/{1}".format(zero, a)

if found == 0:
	print "Does not factor, trying quadratic formula"
	zero = (-b + math.sqrt(b * b - 4 * a * c))/(2 * a)
	zero2 = (-b - math.sqrt(b * b - 4 * a * c))/(2 * a)

print "Factorized: ({2}x + {0})({3}x + {1})({4}){5}".format(zero, zero2, t1, t2, "{0}x + 1".format(a1, b1), remainder).replace("+ -", " - ").replace(" + 0", "").replace(".0","")

