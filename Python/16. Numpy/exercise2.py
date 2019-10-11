# Shape and Reshape "https://www.hackerrank.com/challenges/np-shape-reshape/problem"

import numpy as np

arr = np.array(list(input().strip().split(" ")), int)
print(np.reshape(arr, (3, 3)))
