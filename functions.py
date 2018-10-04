#!/usr/bin/env python3

import numpy as np              # import numpy and sys
import sys

def expo(x):                    # define a function named expo that needs one input x
    return np.exp(x)            # the function will return e^x

def show_expo(n):               # define a subroutine (does not return a value)
    # n needs to be an integer
    for i in range(n):          # loop i values from 0 to n
        print(expo(float(i)))   # call the expo function. also convert i to a 
                                # float to be safe
def main():                     # define main function, no input needed
    n = 10                      # provide a default value for n
    
    if (len(sys.argv)>1):       # sys.argv is the command line arguements. 
        n = int(sys.argv[1])    # if a command line arguement is provided, use it for n
                                    # in cmd: python3 functions.py [insert argv here]
        
    show_expo(n)                # call the show_expo subroutine with the input n
                                # if there are no command line arguements, n is the default 10
if __name__ == '__main__':      # run the main() function
    main()