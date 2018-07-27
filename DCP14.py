import random as r
import math

def get_pi():
    n = 1000000
    count = 0
    for i in range(0, n):
        x = r.uniform(0, 1)
        y = r.uniform(0, 1)
        # is this in area?
        if math.sqrt(x * x + y * y) <= 1:
            count += 1
    return 4 * count / n

