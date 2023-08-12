# input
import sys
input = sys.stdin.readline
N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
ans = 0
# sorting
for _ in range(N):
    mi, mx = min(arr1), max(arr2)
    ans += mi*mx
    arr1.pop(arr1.index(mi))
    arr2.pop(arr2.index(mx))
# output
print(ans)
