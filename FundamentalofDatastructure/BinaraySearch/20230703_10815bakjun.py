import sys
input = sys.stdin.readline
# input
M = int(input())
seto = set(map(int, input().split()))

N = int(input())
arr = list(map(int, input().split()))

# BFS and set
for i in arr:
    if i in seto:
        print(1)
    else:
        print(0)
