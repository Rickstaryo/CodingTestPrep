# 1.Input
N = int(input())
# make a Factorial
# .1 Make with Recursion


def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n*factorial(n-1)
