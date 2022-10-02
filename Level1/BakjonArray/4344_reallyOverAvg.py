# 1. 전체 반복횟수
n = int(input())

# 2. 몇명이나 되는지 확인

for _ in range(n):
    data = list(map(int, input().split()))
    avg = sum(data[1:])/data[0]
    cnt = 0
    for score in data[1:]:
        if score > avg:
            cnt += 1
    rate = cnt/data[0] * 100
    print(f'{rate:.3f}%')
