def solution(n):
    #    Timecomplexity will be around N and NlogN
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer
