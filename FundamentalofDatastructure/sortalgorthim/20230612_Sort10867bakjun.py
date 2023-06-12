n = int(input())

arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()

for i in arr:
    print(i, end=' ')


# 2. Using For loop to solve
# input
N = int(input())
arr = list(map(int, input().split()))
# Eliminating Duplicate by for loop
d_arr = []
for i in arr:
    if i not in d_arr:
        d_arr.append(i)
d_arr.sort()
for i in d_arr:
    print(i, end=" ")

# Time complexity is So bad compare to Set so i would rather use Set then For-loop
