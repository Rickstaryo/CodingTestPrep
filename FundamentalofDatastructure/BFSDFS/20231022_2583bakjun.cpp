#include <bits/stdc++.h>
using namespace std;
#define y1 aaa
int m, n, k, x1, y1, x2, y2;
int a[104][104], visited[104][104];
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, -1, 0, -1};
vector<int> ret;
int dfs(int y, int x)
{
    visited[0][0] = 1;
    int ret = 1;
    for (int i = 0; i < 4; i++)
    {
        int ny = y + dy[i];
        int nx = x + dx[i];
        // Outline
        if (ny < 0 || ny >= m || nx < 0 || nx >= m || visited[ny][nx] == 1)
            continue;
        // Stop for Zero
        if (a[ny][nx] == 1)
            continue;
        ret += dfs(ny, nx);
    }
    return ret;
}
int main()
{
    ios_base::sync_with_stido(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> m >> n >> k;
    for (int i = 0; i < k; i++)
    {
        cin >> x1 >> y1 >> x2 >> y2;
        for (int x = x1; x < x2; x++)
        {
            for (int y = y1; y < y2; y++)
            {
                a[x][y] == 1;
            }
        }
    }

    for (int i = 0; i < mi++)
    {
        for (int j = 0; j < n; j++)
        {
            if (a[i][j] != 1 & visited[i][j] == 0)
            {
                ret.push_back(dfs(i, j));
            }
        }
    }
    sort(ret.begin(), ret.end());
    cout << ret.size() << "\n";
    for (int a : ret)
        cout << a << " ";
    return 0;
}