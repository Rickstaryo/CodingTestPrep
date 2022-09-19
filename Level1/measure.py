# for left in range(right):
#     if cnt%2==0:
#         answer +=left
#     else:
#         answer -=left
#     for left in range(n):
#         if left%n==0 :
#             cnt+=1

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += i  # 짝수라면 더해주고
        else:
            answer -= i  # 홀수라면 빼줍니다.

    return answer
