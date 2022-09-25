# https://www.acmicpc.net/problem/2775
T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    floor = [i for i in range(1, n+1)]

    for _ in range(k):
        for i in range(1, n):
            floor[i] += floor[i-1]
    print(floor[-1])
