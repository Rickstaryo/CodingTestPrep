n, l = map(int, input().split())

# 수식

# lx = n - l(l+1)/2
for i in range(l, 101):
    x = n - i * (i + 1) / 2
    if x % i == 0:
        x = int(x / i)
        if x >= -1:
            print(*list(range(x + 1, x + i + 1)))
            break
else:
    print(-1)