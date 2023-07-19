import sys


m, n = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(arr)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    if mid == 0:
        total = 0
        break

    for x in arr:
        if x >= mid:
            total += (x//mid)

    if total >= m:
        start = mid + 1
        result = mid

    else:
        end = mid - 1

print(result)
