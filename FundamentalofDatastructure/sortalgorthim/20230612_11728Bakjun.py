N, M = map(int, input().split())
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))
li = sorted(li1+li2)
print(*li)
