def solution(sides):
    # 1. 가장긴변의 길이는 두변의 길이 합 보다 짧다
    sides.sort()
    if sides[-1] < sides.sum():
        return 1
    return 2


def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2
