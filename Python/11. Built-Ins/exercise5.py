# ginortS "https://www.hackerrank.com/challenges/ginorts/problem"

from string import ascii_lowercase, ascii_uppercase
from functools import reduce


order = ascii_lowercase + ascii_uppercase + "1357902468"
print(reduce(lambda x, y: x + y, sorted(input(), key=order.index)))
