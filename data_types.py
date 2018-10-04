#!/usr/bin/env python3

import numpy as np       

i = 10                          # declare integer i
print(type(i))                  # print the data type of i (int)

a_i = np.zeros(i,dtype=int)     # create an array of zeroes where each zero is an int
print(type(a_i))                # print the data type of a_i (numpy.ndarray)
print(type(a_i[0]))             # print data type of the first element of a_i (numpy.int32)
                                    # in the slides his was int64, I'm not sure why on my computer it says int32
x = 119.0                       # declare a float. You can differentiate them from ints because they have a decimal
print(type(x))                  # print data type of x (float)

y = 1.19e2                      # declare the same float as x but in scientific notation
print(type(y))                  # still a float though

z = np.zeros(i,dtype=float)     # create an arrat of zeroes where each zero is a float
print(type(z))                  # print the data type of z (numpy.ndarray)
print(type(z[0]))               # print the data type of the first element of z (numpy.float64)