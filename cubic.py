#!/usr/bin/python

import sys
import math

def sign(n):
	return n / math.sqrt(n * n)

if len(sys.argv) != 5:
	sys.exit(-1)

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = int(sys.argv[4])

print "Equation: {0}x^3 + {1}x^2 + {2}x + {3}".format(a,b,c,d).replace("+ -", "- ")

factors = []

for i in range(1, abs(d) + 1):
	print "Checking Factor {0}".format(i)
	if abs(d) % i == 0:
		factors.append(i)
		factors.append(-i)
if len(factors) == 0:
	factors = [0]

print "Factors of D: {0}".format(factors)

zero = 0

for x in factors:
	print "checking factor {0}".format(x)
	if a * x * x * x + b * x * x + c * x + d == 0:
		zero = x
		print "Found zero ({0})".format(x)
		break

zero1 = zero

a1 = a
b1 = a1 * zero1 + b
c1 = b1 * zero1 + c
d1 = c1 * zero1 + d


print "Synthetic division: {0}, {1}, {2}, {3}".format(a1, b1, c1, d1)
if d1 == 0:
	print "Synthetic division remainder check successful (d == 0)"
else:
	print "Synthetic division remainder check unsucessful, wat (d == {0})".format(d1)
	sys.exit(-1)

print "Quadratic: {0}x^2 + {1}x + {2}".format(a1, b1, c1).replace("+ -", "- ")

factors = []

for i in range(1, abs(c1 * a1) + 1):
	if abs(c1 * a1) % i == 0:
		factors.append(i)
		factors.append(-i)
print factors

zero2 = 0
zero3 = 0

for x1 in factors:
	for y1 in factors:
		if x1 + y1 == b1:
			print "Found Quadratic pair {0} + {1} = {2}".format(x1, y1, b1).replace("+ -", "- ")
			zero2 = x1
			zero3 = y1

print "Factorized: (x + {0})(x + {1})(x + {2})".format(zero1, zero2, zero3).replace("+ -", "- ")



