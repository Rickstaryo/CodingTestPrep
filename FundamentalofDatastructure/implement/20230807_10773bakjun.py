# input
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    m = int(input())
    if m == 0:
        arr.pop()
    else:
        arr.append(m)
print(sum(arr))


# miss Code
# input
N = int(input())
arr = []
for _ in range(N):
    m = int(input())
    if m == 0:
        arr.pop()
    else:
        arr.append(m)
print(sum(arr))
