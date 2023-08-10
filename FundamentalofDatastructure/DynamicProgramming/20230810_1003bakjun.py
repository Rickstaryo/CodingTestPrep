# Memoraization
arr_zero = [1, 0, 1]
arr_one = [0, 1, 1]


def fibo(n):
    if len(arr_zero) <= n:
        for i in range(len(arr_zero), n+1):
            arr_zero.append(arr_zero[i-1]+arr_zero[i-2])
            arr_one.append(arr_one[i-1]+arr_one[i-2])
    print(arr_zero[n], arr_one[n])


# input
M = int(input())
for i in range(M):
    a = int(input())
    fibo(a)
