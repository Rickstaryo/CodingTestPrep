data = []
for i in range(9):
    n = int(input())
    data.append(n)
maxnum = max(data)
print(maxnum)
print(data.index(maxnum)+1)
