import sys


n, m = map(int, sys.stdin.readline().split())
s = [str(sys.stdin.readline()) for _ in range(n)]  # 집합 s
cnt = 0

# 반복문을 통해 m개의 문자열을 확인
for i in range(m):
    word = str(sys.stdin.readline())

    # 집합 s에 문자열이 포함되어 있으면 카운트
    if word in s:
        cnt += 1

print(cnt)
