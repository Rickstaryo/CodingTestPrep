def solution(n):
    return n % sum([int(c) for c in str(n)]) == 0

    # int 를 input then str(n) become Whole String
