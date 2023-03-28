def solution(n):
    ans = 0
    while n != 1:
        if n % 2 == 0:
            n = n//2
            ans += 1
        else:
            n = (n*3)+1
            ans += 1
        if ans >= 500:
            ans = -1
            break
    return ans
