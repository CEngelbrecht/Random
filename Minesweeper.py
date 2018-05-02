import numpy as np 
from random import randint
'''
Script that generates a NxN array and populates a random number of entries with bombs (the number 50)
, and then populates the rest of the matrix with the corresponding numer of bombs in the vicinity'''

N = 5

A = np.zeros((N,N))
counter = 0 

for i in range(N):
	for j in range(N):
		if randint(1,100) % 3 == 0: 
			A[i][j] = 50
			counter += 1

		else:
			A[i][j] = 0

print(A)
print "\nTotal bombs = {}, which is {} percent of the total".format(counter, (counter/(float(N)*N))*100)

def check_bombs(i,j):
	'''Checks boundary conditions, then returns a counter corresponding to how many bombs exist in a 
		3x3 grid surrounding cell i,j'''

	if A[i][j] == 50:

		return 50 

	if (i == 0):
		#you're on the first row, don't look at row above, i.e. A[i] and A[i+1] only 
		if (j == 0):
			#you're on the first column, don't look at row left, i.e A[j] and A[j+1] only 
			counter = 0
			if A[i][j+1] == 50:
				counter += 1 
			if A[i+1][j] == 50:
				counter += 1
			if A[i+1][j+1] == 50:
				counter += 1
			return counter 
		elif (j == N-1):
			#you're on the last column, only check the previous and current column
			counter = 0 
			if A[i][j-1] == 50:
				counter += 1
			if A[i+1][j-1] == 50:
				counter += 1
			if A[i+1][j] == 50:
				counter += 1
			return counter 
		else:
			#you're between first and last column, but first row: all j's fine, only i and i+1 though
			counter = 0 
			if A[i][j-1] == 50:
				counter += 1
			if A[i][j+1] == 50:
				counter += 1
			if A[i+1][j-1] == 50:
				counter += 1
			if A[i+1][j] == 50: 
				counter +=1 
			if A[i+1][j+1] == 50:
				counter += 1 
			return counter

	if (i == N-1):
		#You're on the last row, only look at current and previous row, i.e A[i] and A[i-1] only 

		if (j == 0):
			#You're on the first column, only need j and j + 1 column
			counter = 0 
			if A[i-1][j] == 50:
				counter += 1
			if A[i-1][j+1] == 50:
				counter +=1 
			if A[i][j+1] == 50:
				counter +=1 
			return counter 
		elif (j == N-1):
			#You're on the last column, only need   j and j - 1 column 
			counter = 0 
			if A[i-1][j-1] == 50:
				counter += 1 
			if A[i-1][j] == 50:
				counter += 1
			if A[i][j-1] == 50:
				counter += 1
			return counter 
		else: 
			#Between first and last columns, need all j's , only i and i -1 though
			counter = 0 
			if A[i-1][j-1] == 50:
				counter += 1
			if A[i-1][j] == 50:
				counter += 1
			if A[i-1][j+1] == 50:
				counter += 1
			if A[i][j-1] == 50:
				counter += 1
			if A[i][j+1] == 50:
				counter += 1

			return counter 

	if (j == 0):

		#You're on the first column. First column first row is taken care of already! 
		counter = 0 
		if A[i-1][j] == 50: 
			counter += 1
		if A[i-1][j+1] == 50: 
			counter += 1
		if A[i][j+1] == 50: 
			counter += 1
		if A[i+1][j] == 50: 
			counter += 1
		if A[i+1][j+1] == 50: 
			counter += 1
		return counter 

	if (j == N-1):

		#You're on the last column. Last column last row is taken care of already 
		counter = 0
		if A[i-1][j-1] == 50: 
			counter += 1
		if A[i-1][j] == 50: 
			counter += 1
		if A[i][j-1] == 50: 
			counter += 1
		if A[i-1][j-1] == 50: 
			counter += 1
		if A[i-1][j] == 50: 
			counter += 1
		return counter

	else: 
		counter = 0 
		if A[i-1][j-1] == 50: 
			counter += 1
		if A[i-1][j] == 50: 
			counter += 1
		if A[i-1][j+1] == 50: 
			counter += 1
		if A[i][j-1] == 50: 
			counter += 1
		if A[i][j+1] == 50: 
			counter += 1
		if A[i+1][j-1] == 50: 
			counter += 1
		if A[i+1][j] == 50: 
			counter += 1
		if A[i+1][j+1] == 50: 
			counter += 1
		return counter 


for i in range(N):
	for j in range(N):
		try: 
			num = check_bombs(i,j)
			A[i][j] = num
		except IndexError as e:
			print("Error!! {}".format(e))
			print(A)


print('\n')
print A