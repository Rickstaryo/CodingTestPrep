# input
M, N = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
print(a[N-1])
