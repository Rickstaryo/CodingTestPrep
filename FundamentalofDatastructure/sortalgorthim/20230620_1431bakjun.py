# Input
N = int(input())
arr = []
for _ in range(N):
    arr.append(input())
# Sorting
# 1.Shorter one come First
# 2.adding number from s erial number


def sum_num(input):
    result = 0
    for i in input:
        if i.isdigit():
            result += i
    return result


# 3. By alphabetic letter
arr.sort(key=lambda x: (len(x), sum_num(x), x))
# Output
print(*arr)
