# Re.start() & Re.end() "https://www.hackerrank.com/challenges/re-start-re-end/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input()
k = input()

pattern = re.compile(k)
r = pattern.search(S)
if not r:
    print("(-1, -1)")
while r:
    print("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(S, r.start() + 1)
