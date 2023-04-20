def solution(food):
    half = ''
    for i in range(1, len(food)):
        half += food[i]//2*str(i)
    return half+'0' + half[::-1]
