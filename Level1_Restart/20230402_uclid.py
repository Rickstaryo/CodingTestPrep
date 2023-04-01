def solution(a, b):
    c, d = max(a, b), min(a, b)

    while d:
        c, d = d, c % d
    answer = [c, int(a*b/c)]

    return answer
