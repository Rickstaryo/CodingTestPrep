# https://growingarchive.tistory.com/146
def solution(A, B):
    if A == B:
        return 0
    # 0. 핵심은 순서를 바꾸어 주는것
    # 1. split 과 join 으로 풀어냄
    # 2. 스와프에대한 생각
    else:
        a = A.split("")

        a[0], a[-1] = a[-1], a[0]
        a.join
        return 1
    answer = 0
    return answer


#  All wrong about the code

def solution(A, B):
    answer = 0
    while answer != len(A):
        if A == B:
            return answer
        A = A[-1]+A[:-1]
        answer += 1

    return -1


def solution(A, B): return (B * 2).find(A)
