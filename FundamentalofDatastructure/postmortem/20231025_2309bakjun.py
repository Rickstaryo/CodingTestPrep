import itertools

array = [int(input()) for _ in range(9)]

for i in itertools.combinations(array, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break

# 2 for   구문으로 해결


array = []
for i in range(9):
    array.append(int(input()))

array.sort()

sum_ = sum(array)

for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if sum_ - array[i] - array[j] == 100:
            for k in range(len(array)):
                if k == i or k == j:
                    pass
                else:
                    print(array[k])
            exit()
