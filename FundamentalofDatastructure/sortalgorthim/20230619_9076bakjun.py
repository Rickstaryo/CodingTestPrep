import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B, C, D, E = sorted(map(int, input().split()))
    if D-B >= 4:
        print("KIN")
    else:
        print(B+C+D)
