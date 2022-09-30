n = int(input())
data = list(map(int, input().split()))

for i in range(n-1):
    a, b = data[0], data[i+1]
    while(a % b != 0):
        r = a % b
        a, b = b, r
    bunmo = data[0]//b
    bunja = data[i+1]//b
    print(f'{bumo}/{bunja}')
