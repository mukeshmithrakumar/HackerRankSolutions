# Incorrect Regex "https://www.hackerrank.com/challenges/incorrect-regex/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for i in range(int(input())):
    try:
        re.compile(input())
        print("True")
    except ValueError:
        print("False")
