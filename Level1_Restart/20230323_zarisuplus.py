def plus(number):
    answer = 0
    while number > 0:
        answer += number % 10
        number = number//10
    return answer
