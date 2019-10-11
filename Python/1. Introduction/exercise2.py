#!/bin/python3

# Python If-Else "https://www.hackerrank.com/challenges/py-if-else/problem"


if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0 or (n % 2 == 0 and 6 < n < 21):
        print("Weird")
    elif n % 2 == 0 and (2 < n < 6 or n > 20):
        print("Not Weird")
