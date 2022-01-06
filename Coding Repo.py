import numpy as np
import math
# function distance between points
def distanceRange(A,B,d1,d2,d3,d4,d5):
    for a in A:
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        for b in B:
            b_a = b - a
            dist = math.hypot(b_a[0],b_a[1],b_a[2])
            if dist >= d1 and dist < d2:
                count1 += 1
            elif dist >= d2 and dist < d3:
                count2 += 1
            elif dist >= d3 and dist < d4:
                count3 += 1
            elif dist >= d4 and dist < d5:
                count4 += 1
            else: 
                continue
        print("count1: %s count2: %s count3: %s count4: %s" % (count1, count2, count3, count4))
    return

# Example
A = np.array([[1,2,3],[4,5,6],[2,6,7],[1,3,6],[3,4,2]])
B = np.array([[2,3,1],[1,4,7],[1,1,1],[2,1,5],[1,5,4]])
d1, d2, d3, d4, d5 = 1, 2, 3, 4, 5
distanceRange(A,B,d1,d2,d3,d4,d5)