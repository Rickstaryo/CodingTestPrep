def solution(k, score):
    ans = []
    # 최하점의 배열을 생성해라
    tmp = []
    for i in score:
        tmp = sorted(tmp.append(score[i]))
        if len(tmp) <= k:
            ans.append(min(tmp))
        else:
            ans.append(min(tmp[-1:-k:-1]))
    return ans
