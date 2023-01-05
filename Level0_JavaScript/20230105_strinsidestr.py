# why it's not working i need to analayze.
def solution(str1, str2):
    return str1.find(str2)

# in 을 이용해 검색


def solution(str1, str2):

    if str2 in str1:
        answer = 1
    else:
        answer = 2

    return answer
