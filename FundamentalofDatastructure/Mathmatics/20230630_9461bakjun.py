# input
arr = [1, 1, 1]
for i in range(3, 101):
    arr.append(arr[i-2]+arr[i-3])

M = int(input())
for _ in range(M):
    print(arr[int(input())-1])
