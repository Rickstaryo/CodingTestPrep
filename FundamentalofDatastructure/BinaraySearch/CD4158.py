# 1. Input
N, M = map(int, input().split())
arr1 = []
arr2 = []
for i in range(N):
    arr1.append(int(input()))
for j in range(N):
    arr2.append(int(input()))

arr1.sort(reverse=True)
arr2.sort(reverse=True)
