# input
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    t1 = int(input())
    arr_t1 = set(map(int, input().split()))
    t2 = int(input())
    arr_t2 = list(map(int, input().split()))
    for i in arr_t2:
        if i in arr_t1:
            print(1)
        else:
            print(0)
