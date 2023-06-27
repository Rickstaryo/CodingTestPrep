# def is_prime(N):
#     if n == 1:
#         return False
#     for i in range(2, int(N**0.5)+1):
#         if N % i == 0:
#             return False
#     return True


# for _ in range(int(input())):
#     num = int(input())

#     a, b = num//2, num//2
#     while a > 0:
#         if is_prime(a) and is_prime(b):
#             print(a, b)
#         else:
#             a -= 1
#             b += 1
# time over
def Goldbach():
    check = [False, False] + [True] * 10000

    for i in range(2, 101):
        if check[i] == True:
            for j in range(i + i, 10001, i):
                check[j] = False

    T = int(input())
    for _ in range(T):
        n = int(input())

        A = n // 2
        B = A
        for _ in range(10000):
            if check[A] and check[B]:
                print(A, B)
                break
            A -= 1
            B += 1


Goldbach()
