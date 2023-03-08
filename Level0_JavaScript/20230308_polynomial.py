def solution(polynomial):
    # x와 x분리하고
    arr = polynomial.split("+")
    xarr = []
    numarr = []
    for i in arr:
        if i in x:
            ii = int(i.replace('', 'x '))
            xarr.append(ii)
        else:
            numarr.append(i)
    return str(sum(xarr))+'x ' + '+ ' + str(sum(numarr))

    def solution(polynomial):
        xnum = 0
        const = 0
        for c in polynomial.split(' + '):
            if c.isdigit():
                const += int(c)
            else:
                xnum = xnum+1 if c == 'x' else xnum+int(c[:-1])
        if xnum == 0:
            return str(const)
        elif xnum == 1:
            return 'x + '+str(const) if const != 0 else 'x'
        else:
            return f'{xnum}x + {const}' if const != 0 else f'{xnum}x'
