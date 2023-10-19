# Input
M, N = map(int, input().split())
arr = []
for i in range(M):
    num, gold, silver, bronze = map(int, input().split())
    arr[i] = [num, gold, silver, bronze]
# sorting out
sort_arr = sorted(arr, key=lambda x: (x[1], x[2], x[3]))
# 3 to print out
print(sort_arr.index(arr[N]))


#
N, K = map(int, input().split())

medals = [list(map(int, input().split())) for _ in range(N)]

medals.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

idx = [medals[i][0] for i in range(N)].index(K)

for i in range(N):
    if medals[idx][1:] == medals[i][1:]:
        print(i+1)
        break
