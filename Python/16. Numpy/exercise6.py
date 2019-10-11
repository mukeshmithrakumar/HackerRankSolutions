# Eye and Identity "https://www.hackerrank.com/challenges/np-eye-and-identity/problem"

import numpy as np
np.set_printoptions(legacy='1.13')

N, M = map(int, input().split())

print(np.eye(N, M, k=0))
