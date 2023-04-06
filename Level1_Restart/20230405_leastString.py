def solution(t, p):
    ans = 0
    for i in range(0, len(t)-len(p)+1):
        if int(t[i:i+len(p)]) <= int(p):
            ans += 1
    return ans
