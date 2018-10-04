#!/usr/bin/env python3

example_dict = {                                # create a dictionary made with curly brackets {}
     'class'        :   'Astr 119',             # left of ':' is the key, 
     'prof'         :   'Brant',                # on the right is the value
     'awesomeness'  :   10                      
 }                                              

print(type(example_dict))                       # prints data type of example_dict (dict)

course = example_dict['class']                  # define var course as the value associated with the key 'class' in example_dict
print(course)                                   # print course

example_dict['awesomeness'] += 1                # find the value associated with the key 'awesomeness' and adds 1 to it

print(example_dict)                             # print the dictionary

for x in example_dict.keys():                   # loop x through all the different keys in examply_dict
    print(x,example_dict[x])                    # print the key and the associated value