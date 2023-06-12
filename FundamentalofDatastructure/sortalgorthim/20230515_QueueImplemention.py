# 파이썬으로 큐를 구현할때는 Collection module에서 제공하는 deque를 이용하자
# from collections import deque

# queue = deque()

# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()
# print(queue)


class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def enqueue(self, item):
        if len(self.queue) == self.max_size:
            print("Overflow!")
            return False
        self.queue.append(item)
        return True

    def dequeue(self):
        if len(self.queue) == 0:
            print("Underflow!")
            return None
        return self.queue.pop(0)


q = Queue(3)

for element in q.queue:
    print(q.queue)
q.enqueue(4)  # prints "Overflow!" and returns False
q.dequeue()  # returns 1
q.dequeue()  # returns 2
q.dequeue()  # returns 3
q.dequeue()  # prints "Underflow!" and returns None
