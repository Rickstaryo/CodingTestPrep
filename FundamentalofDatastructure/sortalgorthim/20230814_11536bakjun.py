# input
N = int(input())
arr = []
for i in range(N):
    arr.append(input())
# sorting

inc, dec = 0, 0
for i in range(N-1):
    if ord((arr[i])[0]) > ord((arr[i+1])[0]):
        dec += 1
    elif ord((arr[i])[0]) < ord((arr[i+1])[0]):
        inc += 1

if inc > 0 and dec == 0:
    print("INCREASING")
elif inc == 0 and dec > 0:
    print("DECREASING")
else:
    print("NEITHER")


# Coding
n = int(input())

arr = []

for _ in range(n):
    name = input()
    arr.append(name)


if sorted(arr) == arr:
    print("INCREASING")
elif sorted(arr, reverse=True) == arr:
    print("DECREASING")
else:
    print("NEITHER")
