# Daily Coding Problem # 14
#
# The area of a circle is defined as πr^2. 
# Estimate π to 3 decimal places using a Monte Carlo method.
# Hint: The basic equation of a circle is x2 + y2 = r2.
#
# Generate a bunch of number pairs from 0 - 1 (x, y coordinates)
# For each generated point, determine if the point lies in the
# upper right quadrant of the unit circle (0 <= x & y <= 1)
# Take the ratio of the number of points in the circle and the 
# total number of random points.  Multiply by 4 to complete the
# remaining quadrants of the unit circle.  The result should be
# an approximation of pi.  The higher n is, the more accurate the
# approximation is.

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

