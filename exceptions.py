#!/usr/bin/env python3

try:                                        # try the following code
    print(a)                                # won't work since we have not defined a
except:                                     # if there is ANY error
    print('a is not defined!')              # print this
    
try:
    print(a)
except NameError:                           # if the error is SPECIFICALLY NameError
    print('a is still not defined!')        # print this
except:                                     # if error is anything else
    print('Something else went wrong.')
    
print(a)                                    # because we didn't use 'try' this will crash our code