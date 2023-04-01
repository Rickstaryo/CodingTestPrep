def solution(arr1, arr2):
    answer = arr1
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] = arr1[i][j]+arr2[i][j]
    return answer


def solution(arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        l = []
        for x, y in zip(a, b):
            l.append(x+y)
        answer.append(l)

    return answer
