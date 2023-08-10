# input
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
arr = []
cnt = 0
for _ in range(M):
    arr.append(int(input()))

# Greedy
arr.sort(reverse=True)

for i in arr:
    cnt += N//i
    N = N % i
# output
print(cnt)
