# 셀프넘버 푸는 법
# 1. 일정한 등식이 보이지않음 -> 셀프넘버를 생성해 전체에서 빼줌

def collect(n):
    n = n+sum(map(int, str(n)))
    return n


# 1. notselfnum을 찾아줌
notselfnum = set()
for i in range(1, 10001):
    notselfnum.add(collect(i))
# 2. 전체에서 notselfnum 빼줌
for j in range(1, 10001):
    if j not in notselfnum:
        print(j)
