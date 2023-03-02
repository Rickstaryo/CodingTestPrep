def solution(s):
    ans = ''
    for alp in "abcdefghijklmnopqrstuvwxyz":
        if 1 == s.count(alp):
            ans += alp
    return ans
