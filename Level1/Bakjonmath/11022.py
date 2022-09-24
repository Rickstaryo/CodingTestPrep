cases = int(input())

for i in range(cases):
    a, b = map(int, input().split())
    ans = a + b
    print("Case #%s: %s + %s = %s" % (i+1, a, b, ans))
#  number 2
T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    print("Case #" + str(i) + ":", A, "+", B, "=", A+B)
