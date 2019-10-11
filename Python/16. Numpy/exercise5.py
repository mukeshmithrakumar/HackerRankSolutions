# Zeros and Ones "https://www.hackerrank.com/challenges/np-zeros-and-ones/problem"

import numpy as np

dim = tuple(map(int, input().split()))

print(np.zeros(dim, dtype=np.int))
print(np.ones(dim, dtype=np.int))
