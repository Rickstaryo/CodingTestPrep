def solution(my_string, num1, num2):
    answer = ''
    box = list(my_string)
    box[num1], box[num2] = box[num2], box[num1]
    return answer.join(box)
