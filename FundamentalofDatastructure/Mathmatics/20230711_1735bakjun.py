def gcd(a, b):
    r = b % a
    if r == 0:
        return a
    return gcd(r, a)


a, b = map(int, input().split())
c, d = map(int, input().split())
n = gcd((a*d+b*c), b*d)
print((a*d+b*c)//n, (b*d)//n)
