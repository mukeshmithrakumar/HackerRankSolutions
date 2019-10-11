# Concatenate "https://www.hackerrank.com/challenges/np-concatenate/problem"

import numpy as np

N, M, P = map(int, input().split())

arr1 = np.array([input().split() for _ in range(N)], int)
arr2 = np.array([input().split() for _ in range(M)], int)

print(np.concatenate((arr1, arr2), axis=0))
