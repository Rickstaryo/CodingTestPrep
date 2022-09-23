def solution(n):
    #    Timecomplexity will be around N and NlogN
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer

# 다른 사람의 방식


def water_melon(n):
    return "수박"*(n//2) + "수"*(n % 2)
