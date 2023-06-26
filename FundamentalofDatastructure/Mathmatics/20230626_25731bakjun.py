def convert(a, b):
    base = ''

    while a > 0:
        a, mod = divmod(a, b)
        base += str(mod)

    return base[::-1]


n, k = map(int, input().split())
nums = str(convert(n, k))

lst = []
tmp = ''
for i in nums:
    if i == '0':
        lst.append(tmp)
        tmp = ''
        continue
    tmp += i
if len(tmp) > 0:
    lst.append(tmp)

result = 0
for i in lst:
    if i.isdigit():
        result += int(i)

print(convert(result, k))
