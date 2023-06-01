# 1. Input set
N = int(input())
arr = []
# 2. Sorting by purpose
for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    arr.append((age, name))
# 2.2 First Sort by Age then Date
arr.sort(key=lambda x: x[0])
# 3. Out put set
for i in arr:
    print(i[0], i[1])
