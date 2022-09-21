# Wrong solving python code
# def solution(n):
#     answer = [n.length]
#     cnt= 0
#     while(n>0):
#         answer[cnt] = n%10
#         n /= 10
#         cnt +=1
#     return answer


def solution(n):
    a = []

    while n > 1:
        a.append(int(n % 10))
        n /= 10

    return a
