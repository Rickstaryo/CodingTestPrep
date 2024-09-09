n, h, j = map(int, input().split())
cnt = 0
while h != j:
    h -= h//2
    j -= j//2
    cnt += 1
print(cnt)
