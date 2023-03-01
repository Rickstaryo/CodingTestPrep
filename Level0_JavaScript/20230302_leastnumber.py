def solution(a, n): return sorted(a, key=lambda x: (abs(x-n), x))[0]
