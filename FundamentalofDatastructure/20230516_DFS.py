# Example of map function in Python
numbers = [1, 2, 3, 4, 5]


def square(x):
    return x * x


squares = list(map(square, numbers))
print(squares)


# Example
# 음료수 얼려 먹기

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    # Making Recursion Then need to make an exception
    if x < 0 or x >= n or y <= -1 or y >= m:
        return False
    # Make a node visited yet
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)
