N = int(input())
cnt = 0
for _ in range(N):
    a, b = map(int, input().split())
    cnt += a*(b)
print(cnt)
