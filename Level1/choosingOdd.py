
from itertools import combinations


def prime_number(x):
    answer = 0
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            answer += 1
    return 1 if answer == 1 else 0


def solution(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums, 3)])
