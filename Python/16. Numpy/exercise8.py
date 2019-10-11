# Floor, Ceil and Rint "https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem"

import numpy as np
np.set_printoptions(sign=' ')

arr = list(map(float, input().split()))

print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))
