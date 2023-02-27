def solution(n):
    answer = 1
    for i in range(1, n+1):
        answer = i*answer
        if n < answer:
            return i-1
        elif n == answer:
            return i
