# 변환
n, k = map(int, input().split())

print(int(sum([int(i) for i in str(int(str(n), k)).split('0') if i != '']), k))
