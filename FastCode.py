import random
import numpy as np

n = 0
m = 1000000

for i in range(m):
    x = np.array([random.random() for _ in range(4)])
    x.sort()
    d = [x[i+1] - x[i] for i in range(3)]
    d.append(1 - x[3] + x[0])
    for j in range(4):
        if d[j] > 0.25:
            k = j
            break
    ranges = [x[k]]
    for j in range(3):
        t = ranges[-1] + 0.25
        ri = 1 - t if t >= 1 else t
        ranges.append(ri)
    ranges.sort()
    cond = [ranges[i] <= x[i] < (i+1)*0.25 for i in range(3)]
    cond.append(ranges[3] <= x[3])
    if all(cond):
        n += 1

print(n/m*4)
print(32*n/m)
