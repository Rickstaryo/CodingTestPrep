X, Y = map(int, input().split())
z = (Y*100)//X
start, end = 0, X
res = X
if z >= 99:
    print(-1)
else:
    while start <= end:
        mid = (start+end)//2
        if ((Y+mid)*100)//(X+mid) >= z:
            res = mid
            end = mid-1
        else:
            start = mid+1
    print(res)
