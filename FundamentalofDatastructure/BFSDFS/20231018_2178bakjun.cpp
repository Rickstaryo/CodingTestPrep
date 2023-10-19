#include <bits/stdc++.h>
using namespace std;
// n,m,adj,visited, queue, bfs,nx,ny,x,y
const int max_n = 104;
int n, m, adj[max_n][max_n], visited[max_n][max_n], x, y;
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};
int main()
{
    // input
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%1d", &adj[i][j]);
        }
    }
    // bfs process
    queue<pair<int, int>> q;
    visited[0][0] = 1;
    q.push({x, y});
    while (q.size())
    {
        visited[x][y] = 1;
        tie(y, x) = q.front();
        q.pop();
        for (int i = 0; i < n; i++)
        {
            int ny = y + dy[i];
            int nx = x + dx[i];
            // condition to check
            if (ny < 0 || n <= ny || nx < 0 || m <= nx || adj[ny][nx] == 0)
                continue;
            if (visited[ny][nx])
                continue;
            visited[ny][nx] = visited[y][x] + 1;
            q.push({ny, nx});
        }
    }
    scanf("%d", &visited[n - 1][m - 1]);
    return 0;
}