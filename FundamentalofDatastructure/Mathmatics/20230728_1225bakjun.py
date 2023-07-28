import sys
a, b = map(list, sys.stdin.readline().split())

A = list(map(int, a))
B = list(map(int, b))

print(sum(A)*sum(B))
