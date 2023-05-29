# 1. Recursion Way to Implement
def binary_search_recursion(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursion(arr, target, low, mid - 1)
    else:
        return binary_search_recursion(arr, target, mid + 1, high)

# 2.while-loop to Solve


def binary_search_for_loop(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
