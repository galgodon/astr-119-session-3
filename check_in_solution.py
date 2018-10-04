#!/usr/bin/env python3

import numpy as np          # imports the package numpy and gives it the alias np
                            # for ease of access
def main_func():
	i = 0                   # set initial conditions
	x = 119.0               # note that the '.0' is needed to make sure x is a float and not an int
	
	for i in range(120):    # loops from 1 to 119 inclusive (does not include 120)
		if i%2==0:          # if 'i' is even, i%2 will be 0. Note: == is boolean equal
			x += 3          # take what x was and add 3
		else:               # if the above is NOT true (in this case if 'i' is odd)
			x -= 5          # take what x was and subtract 5
			
	s = '{:0.2e}'.format(x) # format x to have 2 decimal places. 'e' makes it scientific notation
	                        # other way is s = '%3.2e' % x
	                        			# print 3 numbers, 2 after the decimal place.
	print(s)                # prints the variable s
	
if __name__ == '__main__':  # if we are in the main function
	main_func()             # runs the function main_func
                            # even though it has no input, there still must be open and closed
                            # parentheses because it is a function