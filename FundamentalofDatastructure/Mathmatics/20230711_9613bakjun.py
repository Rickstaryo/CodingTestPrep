import sys
import math
input = sys.stdin.readline

for _ in range(int(input())):
    a = list(map(int, input().split()))
    n, nums, r = a[0], a[1:], 0

    for i in range(n-1):
        for j in range(i+1, n):
            r += math.gcd(nums[i], nums[j])
    print(r)

# MY solution


def gcd(a, b):
    r = b % a
    if r == 0:
        return a
    return gcd(r, a)


def gcdList(arr, n):
    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            cnt += gcd(arr[i], arr[j])
    return print(cnt)


N = int(input())
for _ in range(N):
    arr = list(map(int, input().split()))
    n, arr = arr[0], arr[1:]
    gcdList(arr, n)
