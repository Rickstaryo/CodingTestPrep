# def solution(k, score):
#     ans = []
#     # 최하점의 배열을 생성해라
#     tmp = []
#     for i in score:
#         tmp = sorted(tmp.append(score[i]))
#         if len(tmp) <= k:
#             ans.append(min(tmp))
#         else:
#             ans.append(min(tmp[-1:-k:-1]))
#     return ans


def solution(k, score):
    ans = []
    # 최하점의 배열을 생성해라
    tmp = []
    for i in score:
        if len(tmp) < k:
            tmp.append(i)
        else:
            if min(tmp) < i:
                tmp.remove(min(tmp))
                tmp.append(i)
        ans.append(min(tmp))
    return ans
