import numpy as np
import sys
import time

start = time.time()


s = range(1000)
print(sys.getsizeof(s))


d = np.arange(1000)
print(d.size)