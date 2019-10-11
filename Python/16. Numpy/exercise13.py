# Inner and Outer "https://www.hackerrank.com/challenges/np-inner-and-outer/problem"

import numpy as np

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(np.inner(a, b))
print(np.outer(a, b))
