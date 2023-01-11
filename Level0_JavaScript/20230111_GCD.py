def solution(n):
    answer = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            answer += 1
    return answer*2-1 if n**0.5 % 1 == 0 else answer*2
