# 1.변수 선언
target_num = int(input())
result = 0

# 2. 탐색
for i in range(1, target_num+1):
    data = list(map(int, str(i)))
    result = i + sum(data)
    if result == target_num:
        print(i)
        break
    if i == target_num:
        print(0)
