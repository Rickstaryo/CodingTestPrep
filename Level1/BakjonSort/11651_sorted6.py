import sys
input = sys.stdin.readline

n = int(input())

data = []
for i in range(n):
    x, y = map(int, input().split())
    data.append([y, x])
sorted_data = sorted(data)
for y, x in sorted_data:
    print(x, y)
