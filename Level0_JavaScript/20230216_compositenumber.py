def solution(n):
    answer = 0
    for i in range(4, n+1):
        if i % 2 == 0 or i % 3 == 0:
            answer += 1
    return answer

    # Critically wrong to build what ? because it need another for to search
    def solution(n):
        answer = 0
        for i in range(4, n+1):
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    answer += 1
                    break
        return answer
