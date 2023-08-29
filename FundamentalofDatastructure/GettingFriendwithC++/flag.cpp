#include <string>
#include <vector>

using namespace std;

int solution(int a, int b, bool flag)
{
    int answer = 0;
    if (flag)
    {
        return a + b;
    }
    else
    {
        return a - b;
    }
}