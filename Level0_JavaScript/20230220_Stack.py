import sys
n = int(sys.stdin.readline())
for i in range(n):
    flag = True
    stack = []
    vps = sys.stdin.readline()
    for v in vps:
        if v == '(':
            stack.append(v)
        elif v == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                flag = False
                break
    if len(stack) == 0 and flag == True:
        print('YES')
    else:
        print('NO')
