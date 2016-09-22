import sys
import math

def stop(a, c, i):
	if abs(a * c) > 1000:
		return abs (a * c) / i > 2
	else:
		return 1

if len(sys.argv) != 4:
	print "Usage: quadratic.py a b c, when the equation is ax^2 + bx + c"
	sys.exit(-1)

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

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
		print "Testing {0} and {1}".format(x,y)
		if x + y == b and x * y == a * c:
			print "Found Quadratic pair {0} + {1} = {2} & {0} * {1} = {3} * {4}".format(x, y, b, a, c).replace("+ -", "- ")
			zero = x
			zero2 = y
			found = 0

t1 = ""
t2 = ""

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

if found:
	print "Factorized: ({2}x + {0})({3}x + {1})".format(zero, zero2, t1, t2).replace("+ -", "- ")
else:
	print "Does not factor, trying quadratic formula"
	print "Quadratic formula zero #1 = {0}".format((-b + math.sqrt(b * b - 4 * a * c))/(2 * a))
	print "Quadratic formula zero #2 = {0}".format((-b - math.sqrt(b * b - 4 * a * c))/(2 * a))



