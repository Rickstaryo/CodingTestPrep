# 1. n개
n = int(input())
# 2. data
data = list(map(int, input().split()))
modify_data = []
max_score = max(data)

for score in data:
    modify_data.append(score/max_score * 100)
    # 3. 변경된 데이터
test_avg = sum(modify_data)/n
print(test_avg)
