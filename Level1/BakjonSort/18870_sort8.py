#먼저, 좌표 압축이라는 것은 여러 곳에 흩뿌려진 좌표들을 연속된 수들로 모아 압축하는 것을 말한다.

# 예를 들어, 다음과 같은 좌표가 있다고 하자.

# [1, 10, 10000, 1000000]

# 이렇게 네 점의 좌표가 있을 때, 좌표는 네 개 이지만 좌표값이 1부터 1,000,000 까지 있다.

# 하지만 이 좌표를 압축하여 순서대로 표현하면 [0, 1, 2, 3] 이 된다.
# 즉, 작은 값부터 시작해서 0부터 인덱스를 부여하는 방식이다.
# 1이 가장 작으므로 0이되고 10이 1, 10000이 2, 1000000이 3이 되는 것이다.

import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr2 = []

arr2 = list(sorted(set(arr)))

dic = {arr2[i]:i for i in range (len(arr2))}

for i in arr:
  print(dic[i],end=' ')
