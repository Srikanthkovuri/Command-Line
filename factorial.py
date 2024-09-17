#!usr/bin/python3
"""This module will print numeric operations
   i.e factorial
"""
import sys
result = 1
given_num=int(sys.argv[-1])
for index in range(1,given_num+1):
    if index == 'numeric.py':
        result=1
    result*=int(index)
print(f"factorial of {given_num} = {result}") 
