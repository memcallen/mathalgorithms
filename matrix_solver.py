#!/usr/bin/python

import operator
import numpy as np
import sys
import random
from fractions import Fraction

class Matrix:
	
	def __init__(self, data): #data=a 2d array containing all matrix elements
		self.data = data
	
	def getRow(self, rownum):
		return self.data[rownum - 1]
	
	def setRow(self, rownum, row=None):
		self.data[rownum - 1] = row
	
	def get(self, row, col):
		return self.data[row - 1][col - 1]
	
	def set_(self, row, col, num):
		self.data[row][col] = num
	
	def doRow(self, process): #[5, 'R2', '+', 3, 'R3', 'R3']
		
		R_ONE_K = process[0]
		R_ONE = int(process[1][1:])
		OP = process[2]
		R_TWO_K = process[3]
		R_TWO = int(process[4][1:])
		R_EQUAL = int(process[5][1:])
		
		process_dict = {
			'+':operator.add,
			'-':operator.sub,
			'*':operator.mul,
			'/':operator.div
		}
		
		NEW_ROW = []
		
		for val in zip(self.getRow(R_ONE), self.getRow(R_TWO)):
			
			NEW_ROW.append(process_dict.get(OP)(R_ONE_K * val[0], R_TWO_K * val[1]))
			
		self.setRow(R_EQUAL, NEW_ROW)


def parallel(one, two):
	return coincident(one[:3], two[:3])

def coincident(one, two):
	return np.linalg.matrix_rank(np.column_stack((one, two))) == 1

def coincident_(one, two):
	
	div_ = div(one[0],two[0])
	
	for v in zip(one[1:], two[1:]):
		if div(v[0],v[1]) != div_:
			if div(v[1],v[0]) != div_:
				return False
	return np.dot(one, two) != 0

def allParallel(one, two, three):
	return parallel(one, two) and parallel(two, three)

def allCoincident(one, two, three):
	return coincident(one, two) and coincident(two, three)

def twoParallel(one, two, three):
	if parallel(one, two):
		return (True, [1,2])
	if parallel(two, three):
		return (True, [2,3])
	if parallel(three, one):
		return (True, [1,3])
	return (False, None)

def twoCoincident(one, two, three):
	if coincident(one, two):
		return (True, [1,2])
	if coincident(two, three):
		return (True, [2,3])
	if coincident(three, one):
		return (True, [1,3])
	return (False, None)

def coplanar(one, two, three):
	return np.cross(one, two).dot(three) == 0

def checkPlane(matrix):
	
	one = matrix.getRow(1)[:3]
	two = matrix.getRow(2)[:3]
	three = matrix.getRow(3)[:3]
	
	checkPlanesPossible(matrix)
	
	COPL = coplanar(one, two, three)
	TWO_COIN = twoCoincident(one, two, three)
	ALL_COIN = allCoincident(one, two, three)
	TWO_PAR = twoParallel(one, two, three)
	ALL_PAR = allParallel(one, two, three)
	
	if COPL:
		print("All Plane are Coplanar")
		return
	
	if TWO_COIN[0] and not ALL_COIN:
		print("Rows {0} and {1} are coincident".format(TWO_COIN[1][0], TWO_COIN[1][1]))
		return
	
	if ALL_COIN:
		print("All Planes are coincident")
		return
	
	if TWO_PAR[0] and not ALL_PAR:
		print("Rows {0} and {1} are parallel".format(TWO_PAR[1][0], TWO_PAR[1][1]))
		return
	
	if ALL_PAR:
		print("All Planes are parallel")
		return
	
	if coplanar(one, two, three):
		print("All Planes are Coplanar")
		return

def doFrac(num):
	fraction = Fraction(str(num)).limit_denominator(10000)
	if num % 1 == 0:
		return num
	else:
		return "{0}/{1}".format(fraction.numerator, fraction.denominator)

def planePossible(plane):
	
	for v in plane:
		if v != 0:
			return True
	return plane[3] == 0

def planesPossible(one, two, three):
	return planePossible(one) and planePossible(two) and planePossible(three)

def checkPlanesPossible(matrix):
	
	one = matrix.getRow(1)
	two = matrix.getRow(2)
	three = matrix.getRow(3)
	
	if not planesPossible(one, two, three):
		a = [one, two, three]
		for k,v in enumerate(a):
			if not planePossible(v):
				print("Plane {0} isn't possible".format(k + 1))
				sys.exit()
	print "All Planes Possible"
	
def solve(input=None):
	R1 = [random.randint(0,9) for v in range(0, 4)]#[1.0,2.0,3.0,4.0]#[1.0, 1.0, -1.0, -3.0]#[3, -4, 5, 6]
	R2 = [random.randint(0,9) for v in range(0, 4)]#[4.0,3.0,2.0,1.0]#[-4.0, 1.0, 4.0, 7.0]#[5, -6, 7, 8]
	R3 = [random.randint(0,9) for v in range(0, 4)]#[2.0,5.0,3.0,1.0]#[-2.0, 3.0, 2.0, 2.0]#[6, -8, 10, 9]
	
	if input==None:
		matrix = Matrix([R1, R2, R3])
	else:
		matrix = Matrix(input)
	
	print "\nInput Coefficients:"
	
	for r in matrix.data:
		print([round(v) for v in r])
	
	print "\nCheck:"
	
	checkPlane(matrix)
	
	print "\nSolving..."
	
	#spot #1
	ONE_K = matrix.get(1, 1)
	TWO_K = matrix.get(2, 1)
	
	matrix.doRow([TWO_K, 'R1', '-', ONE_K, 'R2', 'R2'])
	
	print(str(matrix.data).replace("][", "]\t["))
	
	#spot #2
	ONE_K = matrix.get(1, 1)
	TWO_K = matrix.get(3, 1)
	
	matrix.doRow([TWO_K, 'R1', '-', ONE_K, 'R3', 'R3'])
	
	print(str(matrix.data).replace("][", "]\t["))
	
	#spot #3
	ONE_K = matrix.get(2, 2)
	TWO_K = matrix.get(3, 2)
	
	matrix.doRow([TWO_K, 'R2', '-', ONE_K, 'R3', 'R3'])
	
	print(str(matrix.data).replace("][", "]\t["))
	
	#spot #4
	ONE_K = matrix.get(3, 3)
	TWO_K = matrix.get(1, 3)
	
	matrix.doRow([TWO_K, 'R2', '-', ONE_K, 'R3', 'R2'])
		
	print(str(matrix.data).replace("][", "]\t["))
	
	#spot #5
	ONE_K = matrix.get(1, 3)
	TWO_K = matrix.get(1, 1)
	
	matrix.doRow([TWO_K, 'R3', '-', ONE_K, 'R1', 'R1'])
	
	print(str(matrix.data).replace("][", "]\t["))
	
	#spot #6
	ONE_K = matrix.get(1, 1)
	TWO_K = matrix.get(3, 1)
	
	matrix.doRow([TWO_K, 'R1', '-', ONE_K, 'R3', 'R3'])
	
	print(str(matrix.data).replace("][", "]\t["))
	
	ONE_DIV = matrix.get(1,1)
	TWO_DIV = matrix.get(2,2)
	THREE_DIV = matrix.get(3,3)
	
	if ONE_DIV != 0:
		matrix.doRow([1.0/ONE_DIV, 'R1', '-', 0, 'R1', 'R1'])
	if TWO_DIV != 0:
		matrix.doRow([1.0/TWO_DIV, 'R2', '-', 0, 'R2', 'R2'])
	if THREE_DIV != 0:
		matrix.doRow([1.0/THREE_DIV, 'R3', '-', 0, 'R3', 'R3'])
	
	print("\nSolution:")
	for r in matrix.data:
		print([round(v) for v in r])
	
	print
	
	checkPlanesPossible(matrix)
	
	print
	
	z = matrix.get(3,4)
	
	y = matrix.get(2,4) - matrix.get(2,3) * z
	#y + az = d
	
	x = matrix.get(1,4) - matrix.get(1, 2) * y - matrix.get(1, 3) * z
	#x + ay + bz = d
	
	print("POI:({0},{1},{2})".format(doFrac(x), doFrac(y), doFrac(z)))

solve()

