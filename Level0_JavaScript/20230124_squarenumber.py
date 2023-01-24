def solution(n):
    for x in range(1, n//2):
        if x**(2) == n:
            return 1
    return 2


def solution(n):
    return 1 if (n ** 0.5) % 1 == 0 else 2
