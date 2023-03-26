def solution(n):
    ls = list(str(n))
    ls.sort(reverse=True)
    return int("".join(ls))
# https://school.programmers.co.kr/learn/courses/30/lessons/12933/solution_groups?language=python3
