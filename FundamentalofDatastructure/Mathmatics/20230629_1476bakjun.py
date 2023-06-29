# input
import sys
a, b, c = map(int, input().split())


def power(a, b, c):
    if b == 0:
        return print(a % c)
    elif b % 2 == 0:
        return print(power((a*a) % c, b//2, c))
    else:
        return print((a*power(a, b-1, c)) % c)


a, b, c = map(int, sys.stdin.readline().split())


def power(a, n):
    if n == 1:
        return a % c
    else:
        div = power(a, n//2)
        if n % 2 == 0:
            return (div*div) % c
        else:
            return (div*div*a) % c


print(power(a, b))
