def solution(number):
    answer = 0
    for i in range(len(number)-2):
        for j in range(i + 1, len(number)-1):
            for k in range(j + 1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer

# 첫번째 아이디어 1. 3중 for 문시간 너무 많이 걸림
