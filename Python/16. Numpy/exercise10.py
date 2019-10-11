# Min and Max "https://www.hackerrank.com/challenges/np-min-and-max/problem"

import numpy as np

n, m = tuple(map(int, input().split()))

arr = np.array([input().split() for _ in range(n)], int)
out = np.min(arr, axis=1)

print(max(out))
