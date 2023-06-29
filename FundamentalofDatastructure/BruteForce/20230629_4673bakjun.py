def gen(n):
    n = n+sum(map(int, str(n)))
    return n


sn = set()

for i in range(1, 10001):
    sn.add(gen(i))

for j in in range(1, 10001):
    if j not in sn:
        print(j)
