n, m = map(int, input().split())
data = [True]*(m+1)
data[0] = False
data[1] = False

for i in range(2, int(m**0.5)+1):
    if data[i]:
        for j in range(i*2, m+1, i):
            data[j] = False
for i in range(n, m+1):
    if data[i]:
        print(i)
