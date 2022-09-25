# 에라토스네스 체로 풀기

def isprime(N, M):
    data = [False, False]+[True for i in range(2, M+1)]

    for i in range(2, int(M**0.5)+1):
        if data[i] == True:
            for j in range(i*2, M+1, i):
                data[j] = False
    return [i for i in range(N, M+1) if data[i] == True]


N = int(input())
M = int(input())

result = isprime(N, M)

if len(result) != 0:
    print(sum(result))
    print(result[0])
else:
    print(-1)
