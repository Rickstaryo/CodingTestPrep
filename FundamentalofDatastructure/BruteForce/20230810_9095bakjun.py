# Dynamic Programming
import sys
arr = [0]*11
arr[1] = 1
arr[2] = 2
arr[3] = 4
for i in range(4, 11):
    arr[i] = sum(arr[i-3:i])


# Input
N = int(input())
for _ in range(N):
    print(arr[int(input())])
# Bruteforce

# Output

# DFS Style
read = sys.stdin.readline


def dfs(num):
    if arr[num] > 0:
        return arr[num]
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        arr[num] = dfs(num-1) + dfs(num-2) + dfs(num-3)
        return arr[num]


T = int(sys.stdin.readline())
for _ in range(T):
    l = int(read())
    arr = [0] * (l+1)
    print(dfs(l))
