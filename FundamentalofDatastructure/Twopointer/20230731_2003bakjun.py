import sys

# input
n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
start, end = 0, 1
count = 0
# Twopoint algorithm

while (start <= end and end <= n):

    total = sum(arr[start:end])

    if (total < m):
        end += 1

    elif (total > m):
        start += 1

    else:
        count += 1
        end += 1

print(count)
