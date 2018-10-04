#!/usr/bin/env python3

x = [0.0, 3.0, 5.0, 2.5, 3.7]   # create an array called x. (an array is a list where every element is the same type)
print(type(x))                  # print data type of x (list)

x.pop(2)                        # delete the 3rd element of x (position 2 since we start at position 0)
print(x)                        # print the new x

x.remove(2.5)                   # remove any element of x that is 2.5
print(x)                        # print new x

x.append(1.2)                   # add 1.2 to the end of x
print(x)                        # print new x

y = x.copy()                    # define y as a copy of x
print(y)                        # print y, it will be identical to x

print(y.count(0.0))             # count how many elements are 0.0

print(y.index(3.7))             # outputs the index of the first element that is 3.7

y.sort()                        # sort the elements of y in numerical order
print(y)                        # print new y

y.reverse()                     # reverse the order of y
print(y)                        # print new y

y.clear()                       # clear all elements of y
print(y)                        # print new y