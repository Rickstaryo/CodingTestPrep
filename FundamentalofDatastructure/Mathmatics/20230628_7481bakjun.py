# Greedy Algorithm
import sys


def atm(arr, n):
    arr_p = []
    for i in sorted(arr, reverse=True):
        arr_p.append(int(n//i))
        n = int(n % i)
    if n == 0:
        print(arr_p[0], arr_p[1])
    else:
        print("Impossible")


# Input
N = int(input())
# output
for i in range(N):
    arr = list(map(int, input().split()))
    atm(arr[:1], arr[2])


def print_bills(a, b, s):
    swap = False
    if a > b:
        a, b = b, a
        swap = True
    assert b != 0
    for x in range(b):
        if a * x <= s and a * x % b == s % b:
            y = (s - a * x) // b
            if swap:
                x, y = y, x
            sys.stdout.write(f'{x} {y}\n')
            return
    sys.stdout.write('Impossible\n')


t = int(sys.stdin.readline())
for _ in range(t):
    a, b, s = (int(x) for x in sys.stdin.readline().split())
    print_bills(a, b, s)


main()
