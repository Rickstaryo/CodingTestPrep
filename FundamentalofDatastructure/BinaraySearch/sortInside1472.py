# 1 Input
a = list(map(int, input()))
# 2. sort
a.sort(reverse=True)
# 3. output
for i in a:
    print(i, end='')
