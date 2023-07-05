n = input()

for i in range(len(n)):
    if n[i:] == n[i:][::-1]:
        print(len(n)+i)
        break
