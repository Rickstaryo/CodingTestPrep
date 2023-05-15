# 파이썬으로 큐를 구현할때는 Collection module에서 제공하는 deque를 이용하자
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()
print(queue)
