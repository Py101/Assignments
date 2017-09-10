'''
my first program in python
'''

import sys
numbers = sys.argv[1:]
a,b = int(numbers[0]),int(numbers[1])

print("the number you've passed are:")
print(a,b)

print("a+b=", a+b)