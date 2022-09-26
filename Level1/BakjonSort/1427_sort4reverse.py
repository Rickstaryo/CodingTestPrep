# https://www.acmicpc.net/problem/1427
a = list(map(int, input()))
a.sort(reverse=True)

for i in a:
    print(i, end='')
