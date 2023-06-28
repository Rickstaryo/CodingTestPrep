
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
# input

N = int(input())
Q = []
for _ in range(N):
    n = float(input())
    heappush(Q, n)
# out put
for _ in range(7):
    n = heappop(Q)
    print(f'{n:.3f}')
