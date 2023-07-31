tc = int(input())
for i in range(tc):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    aIdx = 0
    bIdx = 0
    cnt = 0
    while aIdx < n and bIdx < m:
        if A[aIdx] > B[bIdx]:
            cnt += m - bIdx
            aIdx += 1
        else:
            bIdx += 1
    print(cnt)


# Failure code
# #Twopointer
# def twopointer(arr1,arr2):
#     cnt=0
#     for i in arr1:
#         for j in arr2:
#             if i>j:
#                 cnt+=1
#     return cnt
# #input
# T=int(input())

# for _ in range(T):
#     M,N=map(int,input().split())
#     arr1=list(map(int,input().split()))
#     arr2=list(map(int,input().split()))
#     #output
#     print(twopointer(arr1,arr2))
