import numpy as np
import time

st = time.time()
array = np.array([num*num if num%2 == 0 else 0 for num in range(101)])
et = time.time()
print(st-et)

print(array)