N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)  # 이분탐색 검색 범위 설정
