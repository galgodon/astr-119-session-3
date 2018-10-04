#!/usr/bin/env python3

import numpy as np                # import numpy under the alias np

def main():
	i = 0                         # declare integers
	n = 10
	x = 119.0                     # declare floating point by using decimals
	
	# using numpy to declare arrays quickly
	
	y = np.zeros(n,dtype=float)   # creates an array 'n' long of zeroes, each zero is a float
	
	# we can use a for loop to iterate with a variable
	
	for i in range(n):            # loops i from 0 to n-1
		y[i] = 2.0 * float(i) + 1 # sets the ith element of y to a value of the equation. 
		                          # Turned 'i' into a float to make sure it works with the equation
		                          
	# we do not have to loop over a range of numbers, you can loop over the elements in an array
	for y_element in y:           # set y_element as a dummy variable to represent the elements of y
		print(y_element)
		
if __name__ == '__main__':
	main()