def solution(e):
    data = list(map(int, split()))
    return str(min(data)) + " " + str(max(data))
