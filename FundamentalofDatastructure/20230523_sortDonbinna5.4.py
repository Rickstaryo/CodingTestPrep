# 순서대로 해서 가장 작은 것과 비교할것
# 1.input
N, k = int(input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# sorting
arr1.sort()
arr2.sort(reverse=True)

for i in range(k):
    if arr1[i] < arr2[i]:
        arr1[i], arr2[i] = arr2[i], arr1[i]
    else:
        break
print(sum(arr1))
