class_num = 1
for _ in range(k):
    arr = list(map(int, input().split()))
    cnt = arr[0]
    score = sorted(arr[1::], reverse=True)

    max_val = max(score)  # 큰 값
    min_val = min(score)  # 작은 값
    gap_val = score[0] - score[1]  # gap 초기화
    for i in range(2, len(score)):
        gap_val = max(gap_val, score[i - 1] - score[i])

    print('Class', class_num)
    print('Max', max_val, end=", ")
    print('Min', min_val, end=", ")
    print('Largest gap', gap_val)
    class_num += 1
