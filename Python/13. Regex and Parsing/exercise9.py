# Hex Color Code "https://www.hackerrank.com/challenges/hex-color-code/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
import sys

[print(j) for i in sys.stdin for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})', i, re.I)]

# print(*re.findall("(?<!\n)#(?i:[\\da-f]{3}){1,2}", sys.stdin.read()), sep='\n')
