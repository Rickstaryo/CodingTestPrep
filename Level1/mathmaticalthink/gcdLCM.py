# https://school.programmers.co.kr/learn/courses/30/lessons/12940?language=python3
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)

    while d:
        c, d = d, c % d
    answer = [c, int(a*b/c)]

    return answer
