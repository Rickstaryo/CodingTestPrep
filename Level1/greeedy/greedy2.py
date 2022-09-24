n, m = map(int, input().split())

for i in range(n):
    data = list(map(int, input().split()))
    min_Value = min(data)
    result = max(min_Value, result)
print(result)
