def solution(order):
    answer = 0
    for i in str(order):
        if i in ['3', '6', '9']:
            answer += 1
    return answer

    def solution(order):
        return str(order).count("3") + str(order).count("6") + str(order).count("9")
