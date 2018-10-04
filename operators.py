#!/usr/bin/env python3            # makes the terminal know this is in python

x = 9          #Set variables
y = 3

#Arithmetic Operators
print(x+y)     # Addition
print(x-y)     # Subtraction
print(x*y)     # Multiplication
print(x/y)     # Division
print(x%y)     # Modulus (remainder)
print(x**y)    # Exponentiation (to the power of)
x = 9.191823   # Make x into a complicated float to show the effect of floor division
print(x//y)    # Floor Division (divide but get rid of the decimal will ALWAYS round down)
                   # how many whole times does y go into x
# Assignment Operators
x = 9          # set x back to 9. Single equal ASSIGNS the value. Double equals is boolean
x += 3         # take the previous value of x and add 3. So x is now 12
print(x)
x = 9          # set x back to 9. 
x -= 3         # take the previous value of x and subtract 3. So x is now 6
print(x)
x = 9          # set x back to 9
x *= 3         # take the previous value of x and multiply by 3. x = 27
print(x)
x = 9          # set x back to 9
x /= 3         # take the previous value of x and divide 3. x = 3
print(x)
x = 9          # set x back to 9
x **= 3        # take the previous value of x and put it to the power of 3. x = 9^3
print(x)

# Comparison Operators - Booleans
x = 9
y = 3
print(x==y)    # is x the same as y? In this case False
print(x!=y)    # is x different than y? In this case True
print(x>y)     # is x greater than y? In this case True
print(x<y)     # is x less than y? In this case False
print(x>=y)    # is x greater than or equal to y? In this case True
print(x<=y)    # is x less than or equal to y? In this case False