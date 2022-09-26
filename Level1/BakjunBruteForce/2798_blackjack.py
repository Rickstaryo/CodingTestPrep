# if 구문안에서 대소를 비교하는것도 가능하다
# Brute Force
from itertools import combinations
# 1. 변수선언
card_num, target_num = map(int, input().split())
card_list = list(map(int, input().split()))
biggest_num = 0

for cards in combinations(card_list, 3):
    temp_sum = sum(cards)
    if biggest_num < temp_sum <= target_num:
        biggest_num = temp_sum
print(biggest_num)
