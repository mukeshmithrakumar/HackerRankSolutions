#!/bin/python3

# Capitalize! "https://www.hackerrank.com/challenges/capitalize/problem"

import os


# Complete the solve function below.
def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s


# A better way to do this:
# def solve(s):
#     a_string = s.split(' ')
#     return(' '.join((word.capitalize() for word in a_string)))
# This is better because replace() method inside the loop creates copies of string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
