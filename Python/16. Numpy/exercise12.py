# Dot and Cross "https://www.hackerrank.com/challenges/np-dot-and-cross/problem"

import numpy as np

N = int(input())

A = np.array([input().split() for _ in range(N)], int)
B = np.array([input().split() for _ in range(N)], int)

print(np.matmul(A, B))
