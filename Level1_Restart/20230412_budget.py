def solution(d, budget):
    answer = 0
    sum = 0
    sortD = sorted(d)
    for i in sortD:
        if (sum+i) <= budget:
            sum += i
            answer += 1
    return answer
