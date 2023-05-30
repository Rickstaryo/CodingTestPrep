# 입력
N = int(input())
A = set(map(int, input().split()))  # 탐색 시간을 줄이기 위해 set으로 받음
M = int(input())
arr = list(map(int, input().split()))

for num in arr:				# arr의 각 원소별로 탐색
    print(1) if num in A else print(0)  # num이 A 안에 있으면 1, 없으면 0 출력
