#!/usr/bin/env python3

s = 'I am a string.'            # declare a string s
print(type(s))                  # print type of s (str)

yes = True                      # declare a boolean
print(type(yes))                # print type of yes (bool)

no = False                      # declare the other boolean
print(type(no))                 # also will be bool

alpha_list = ['a','b','c']      # create a list with 3 elements. lists made with square brackets []
print(type(alpha_list))         # prints the type of alpha_list (list)
print(type(alpha_list[0]))      # prints type of first element of alpha_list (str)
alpha_list.append('d')          # append or add the string 'd' to alpha_list
print(alpha_list)               # prints the list edited list

alpha_tuple = ('a','b','c')     # create a tuple (tuples are like lists but can't be changed)
print(type(alpha_tuple))        # print the type of alpha_tuple (tuple)

try:                            # try to execute the following code
    alpha_tuple[2] = 'd'        # assign the 3rd element (position 2) the string 'd'
except TypeError:               # if the above code raises a TypeError (which it will since we cannot change tuples)
    print("We can't add elements to tuples!")   # print this if error is TypeError
print(alpha_tuple)              # print alpha_tuple