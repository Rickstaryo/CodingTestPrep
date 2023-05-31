# 1. Binary Code
def binary_search(array, left, right, target):
    while left <= right:
        mid = (left+right)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid+1
        elif array[mid] > target:
            right = mid-1
    return None


n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    x = binary_search(arr1, 0, n-1, i)
    if x != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
# time complexity O((M+N)*logN)

# 2. Count Solution
n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))
for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 3. set()
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))
for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
