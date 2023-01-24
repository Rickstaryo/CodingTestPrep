
def solution(i, j, k):
    answer = 0
    for i in range(i, j+1):
        if str(i).split().count(k) > 0:
            answer += 1
    return answer


"""
# 문제 못품 다시 풀어보자
# 문제점 분석 for 구문으로 돌려서 해결해본다는 생각은 잘하였다 
1. count()
def count(x: str, start: Optional[int]=..., end: Optional[int]=..., /) -> int
S.count(sub[, start[, end]]) -> int
 parameter should be the String not the number and as soon as you put the count it will return the number 
 
"""


def solution(i, j, k):
    answer = 0
    for n in range(i, j + 1):
        answer += str(n).count(str(k))
    return answer
