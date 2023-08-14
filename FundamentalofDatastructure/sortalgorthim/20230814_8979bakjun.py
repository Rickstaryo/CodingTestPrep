# Input
M, N = map(int, input())
arr = []
for i in range(M):
    num, gold, silver, bronze = map(int, input().split())
arr[i] = [num, gold, silver, bronze]
# sorting out
sort_arr = sorted(arr, key=lambda x: (x[1], x[2], x[3]))
# 3 to print out
print(sort_arr.index(arr[N]))
