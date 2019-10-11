# Transpose and Flatten "https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem"

import numpy as np

n, m = map(int, input().split())

arr = np.array([input().split() for _ in range(n)], int)
arr_trans = np.transpose(arr)
print(arr_trans)
print(arr.flatten())
