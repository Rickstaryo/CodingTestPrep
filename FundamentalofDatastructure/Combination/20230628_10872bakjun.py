# input
N = int(input())
ans = 1
# factorial
for i in range(2, N+1):
    if N == 0:
        print(1)
        break
    ans *= i

print(ans)
