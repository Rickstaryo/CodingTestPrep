def solution(n):
    a = []

    while n > 1:
        a.append(int(n % 10))
        n /= 10

    return a
