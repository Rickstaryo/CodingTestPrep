import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
temp = [0]
sum_a = 0
for i in num:
    sum_a += i
    temp.append(sum_a)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(temp[b]-temp[a-1])
