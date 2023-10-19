# input
N = int(input())
arr = []
# Brute force
for _ in range(N):
    w, h = map(int, input().split())
    arr.append((w, h))

for i in arr:
    rank = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")
# output

# The code is likely resulting in an AttributeError because of a typo in the input().spilt() line. spilt() should be split(). The AttributeError occurs because there is no spilt() method in Python.
