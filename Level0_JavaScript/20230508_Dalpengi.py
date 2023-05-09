import sys
import math

# ux-d(x-1)>=m
# x>=(m-d)(u-d)
u, d, m = map(int, sys.stdin.readline().split())
day = (m-d)/(u-d)
print(math.ceil(day))
