# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr


# arr = [64, 25, 12, 22, 11]
# sorted_arr = selection_sort(arr)
# print("Sorted array:", sorted_arr)


# # Understanding Swap

# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]


# arr = [3, 1, 4, 2, 5]
# swap(arr, 1, 3)
# print(arr)  # Output: [3, 2, 4, 1, 5]


# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[min_idx] > arr[j]:
#                 arr[min_idx], arr[j] = arr[j], arr[min_idx]
#     return arr

# print(selection_sort(arr))

arr = [1, 2, 45, 6, 7]


def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


print(insertion_sort(arr))
