# input
n = int(input())
m = n+2

# multiple
arr_n = []
for i in range(1, n+1):
    if n % i == 0:
        arr_n.append([i, n//i])
arr_m = []
for i in range(1, m+1):
    if m % i == 0:
        arr_m.append([i, m//i])

for i in arr_n:
    for j in arr_m:
        if arr_n[0]*arr_m[1]-arr_n[1]*arr_m[0] == n+1:
            print(x[0], -y[0], x[1], y[1])
            exit(0)
print(-1)
