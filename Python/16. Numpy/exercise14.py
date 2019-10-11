# Polynomials "https://www.hackerrank.com/challenges/np-polynomials/problem"

import numpy as np

arr = list(map(float, input().split()))
x = int(input())

print(np.polyval(arr, x))
