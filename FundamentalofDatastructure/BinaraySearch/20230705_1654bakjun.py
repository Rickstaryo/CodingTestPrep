import sys

k, n = map(int, sys.stdin.readline().split())
arr = []

for _ in range(k):
    arr.append(int(input()))
start, end = 1, max(arr)

while (start <= end):
    mid = (start+end)//2
    cnt = 0
    for i in range(k):
        cnt += arr[i]//mid
    if cnt >= n:
        start = mid+1
    else:
        end = mid-1
print(end)
