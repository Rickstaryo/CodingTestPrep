# # input
# N = int(input())
# arr = []
# for _ in range(N):
#     arr.append(input())
# M = int(input())
# arr_search = []
# for _ in range(M):
#     arr_search.append(input())

# # Finding
# for i in range(0, len(arr)-1):
#     if arr[i] == "?":
#         for j in arr_search:
#             if j[0] == (arr[i-1])[0] and j[-1] == (arr[i+1])[-1]:
#                 # output
#                 print(j)
#                 break

N = int(input())
arr = [input() for _ in range(N)]
M = int(input())
cands = [input() for _ in range(M)]

target_idx = arr.index("?")

prv_word = arr[target_idx - 1] if target_idx - 1 >= 0 else None

nxt_word = arr[target_idx + 1] if target_idx + 1 < N else None

for cand in cands:
    flag = True

    if cand in arr:
        flag = False

    if not (prv_word is None or cand[0] == prv_word[-1]):
        flag = False

    if not (nxt_word is None or cand[-1] == nxt_word[0]):
        flag = False

    if flag:
        print(cand)
