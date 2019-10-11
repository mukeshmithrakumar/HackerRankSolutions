# Linear Algebra "https://www.hackerrank.com/challenges/np-linear-algebra/problem"

import numpy as np

n = int(input())

arr = np.array([input().split() for _ in range(n)], float)
arr_det = np.linalg.det(arr)

print(round(arr_det, 2))
