#include <string>
#include <vector>

using namespace std;

int solution(int n)
{
    int answer = 0;
    while (n > 0)
    {
        answer += n % 2 == 0 ? n * n : n;
        n -= 2;
    }
    return answer;
}