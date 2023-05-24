import itertools

vowerl = ('a', 'e', 'i', 'o', 'u')
l, C = map(int, input().split())

arr = input().split(' ')
arr.sort()

for password in itertools.combinations(arr, l):
    count = 0
    for i in password:
        if i in vowels:
            count += 1
    if count >= 1 and count <= l-2:
        print(''.join(password))
