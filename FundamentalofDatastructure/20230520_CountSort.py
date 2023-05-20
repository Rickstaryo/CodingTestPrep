array = [5, 7, 9, 0, 1, 2, 4, 8, 0, 3, 1, 6, 2, 4, 8]

# make a array
count = [0]*(max(array)+1)

# counting
for i in range(len(array)):
    count[array[i]] += 1

# Expressing
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
