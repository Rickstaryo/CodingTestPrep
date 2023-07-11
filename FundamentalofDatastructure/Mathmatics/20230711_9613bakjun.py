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
