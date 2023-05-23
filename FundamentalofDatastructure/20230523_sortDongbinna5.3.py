N = int(input())
arr = []
for i in range(N):
    input_data = input().split()
    arr.append(input_data[0], input_data[1])

arr = arr.sorted(arr, key=lambda student: student[1])
for student in arr:
    print(student[0], end='')


my_list = [(1, 4), (2, 3), (3, 2), (4, 1)]
my_list.sort(key=lambda x: x[1])
print(my_list)
