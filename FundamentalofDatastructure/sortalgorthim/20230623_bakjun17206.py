T = int(input())

a = list(map(int, input().split()))
memo = [0] * 80001
ans = 0

for i in range(80001):
    if i % 3 == 0 or i % 7 == 0:
        ans += i
    memo[i] = ans

for elem in a:
    print(memo[elem])
