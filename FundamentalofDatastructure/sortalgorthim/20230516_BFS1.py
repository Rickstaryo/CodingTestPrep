from collections import deque


def bfs(graph, start, visited):
    # 1. Generate Q
    queue = deque([start])

    # 2. Visiting
    visited[start] = True

    # 3. iterate until become queue
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        # 4. elment connected ,not visited element put on queue
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return True

   # 5. Graph to Express in adjacancy
graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
]

# 6. node to Visited

visited = [False] * 9


bfs(graph, 1, visited)
