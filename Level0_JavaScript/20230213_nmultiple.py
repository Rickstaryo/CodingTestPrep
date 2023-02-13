def solution(n, numlist):
    a = []
    for i in numlist:
        if numlist[i] % n==0:
            a.append(numlist[i])
    return a

# for loops percise Letter 

def solution(n, numlist):
    a = []
    for i in numlist:
        if i % n==0:
            a.append(i)
    return a