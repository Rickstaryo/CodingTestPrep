# Greedy need three step
# Greedy algorithm always ask question about `Minimum` or `Maximum Number`
# 1. Find a idea to solve problem
# 2. Using the sort Algorithm
# 3. Find a solution

n, m, p = map(int, input().split())
data = list(map(int, input().split()))

# 1. Idea to solve 최고의 수이니 최고로 많은 수를 더해서
data.sort()
first = data[n-1]
second = data[n-2]

result = 0
while True:
    for i in range(p):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
print(result)
