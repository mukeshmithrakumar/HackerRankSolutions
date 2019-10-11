# Sum and Prod "https://www.hackerrank.com/challenges/np-sum-and-prod/problem"

import numpy as np

n, m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)], int)

arr_sum = np.sum(arr, axis=0)
print(np.prod(arr_sum))
