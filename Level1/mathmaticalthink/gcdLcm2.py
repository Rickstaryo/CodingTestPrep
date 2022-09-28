import sys

A, B = map(int, sys.stdin.readline().split())
a, b = max(A, B), min(A, B)

while b :
    a = a % b
    a, b = b, a

# gcd
print(a)

# lcm
print(A*B//a)
