import sys

n = int(sys.stdin.readline())
lst = list(set([sys.stdin.readline().strip('\n') for _ in range(n)]))
lst.sort()
lst.sort(key=lambda x: len(x))
print('\n'.join(lst))
