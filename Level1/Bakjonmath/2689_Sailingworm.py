import math
import sys
# Idea 예시 2를 보면 이틀만에 올라감으로 그것을 수학화 시킨다
# 1.ax-b(x-1)>=V  ==> x=(v-b)/(a-b)된다

a, b, v = map(int, sys.stdin.readline().split())
day = (v-b)/(a-b)
print(math.ceil(day))
