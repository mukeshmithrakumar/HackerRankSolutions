# Re.findall() & Re.finditer() "https://www.hackerrank.com/challenges/re-findall-re-finditer/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags=re.I)

print('\n'.join(m or ['-1']))
