def gcd(x, y):
    mod = x % y
    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y


for A in range(1, 30):
    for B in range(1, 30):
        C = int('1' * A)
        D = int('1' * B)
        print(A, B, len(str(gcd(C, D))))
