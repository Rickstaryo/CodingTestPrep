m = int(input())
target = int(input())

arr = list(map(int, input().split()))
arr.sort()
cnt = 0
start, end = 0, m-1
while start < end:
    if arr[start]+arr[end] == target:
        cnt += 1
        start += 1
        end -= 1
    elif arr[start]+arr[end] < target:
        start += 1
    else:
        end -= 1
print(cnt)
