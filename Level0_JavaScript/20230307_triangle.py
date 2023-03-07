def solution(sides):
    # 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
    # IDK<sum(sides)
    #  max(sides)<min(sides)+IDK
    # max(sides)-min(sides)<IDK<sum(sides)
    return sum(sides) - max(sides)+min(sides)-1
