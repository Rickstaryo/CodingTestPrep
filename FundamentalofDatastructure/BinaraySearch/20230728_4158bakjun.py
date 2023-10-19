import sys
while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break
    dic = {}
    Cd_count = 0
    for _ in range(N):
        Cd = int(sys.stdin.readline())
        dic[Cd] = 1

    for _ in range(M):
        Cd = int(sys.stdin.readline())
        if Cd in dic:
            Cd_count += 1

    print(Cd_count)
