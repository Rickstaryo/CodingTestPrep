# https://www.acmicpc.net/status?user_id=ricky_9&problem_id=10950&from_mine=1
#  x 위치엔 range, 리스트 등의 자료형은 올 수 있지만, int 자료형은 오지 못합니다.
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(a+b)
