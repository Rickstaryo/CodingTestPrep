# input
N = int(input())
arr1 = list(map(int, input().split()))


for i in range(1, N):
    arr1[i] = max(arr1[i], arr1[i-1]+arr[i])

print(max(arr1))
