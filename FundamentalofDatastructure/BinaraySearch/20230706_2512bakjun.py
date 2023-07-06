# input
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
budget = int(input())
start, end = 0, max(arr)
bs(start, end, arr)

# BS to find


def bs(start, end, arr):
    mid = (start+end)//2
    cnt = 0
    while start <= end:
        for i in arr:
            if i > mid:
                cnt += mid
            else:
                cnt += i
        if cnt <= budget:
            start = mid+1
        else:
            end = mid-1


return print(end)
