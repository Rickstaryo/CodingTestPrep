def solution(n):
    for i in range(1, n):
        if n % i == 1:
            return i
def solution(n):
    answer = 0

    for divisior in range(2, (n-1)//2+1) : #2부터~반값까지 
        if (n-1) % divisior == 0: #약수가 있다면
            answer = divisior 
            break #탈출
        else: 
            answer = n-1 #약수가 없다면 본인
    return answer