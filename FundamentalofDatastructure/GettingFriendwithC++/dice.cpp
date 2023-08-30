#include <string>
#include <vector>
#include <cmath> //C++
using namespace std;

int solution(int a, int b, int c)
{
    int answer = 0;
    answer += a + b + c;
    if (a == b && b == c)
    {
        answer = (pow(a, 3) + pow(b, 3) + pow(c, 3)) * (pow(a, 2) + pow(b, 2) + pow(c, 2)) * answer;
    }
    else if (a == b || b == c || c == a)
    {
        answer = (pow(a, 2) + pow(b, 2) + pow(c, 2)) * answer;
    }
    else
    {
        answer = a + b + c;
    }
    return answer;
}

// Much better code
#include <string>
#include <vector>
#include <cmath> //C++
using namespace std;

int solution(int a, int b, int c)
{
    int answer = 0;
    answer += a + b + c;
    if (a == b && b == c)
    {
        answer = (pow(a, 3) + pow(b, 3) + pow(c, 3)) * (pow(a, 2) + pow(b, 2) + pow(c, 2)) * answer;
    }
    else if (a == b || b == c || c == a)
    {
        answer = (pow(a, 2) + pow(b, 2) + pow(c, 2)) * answer;
    }
    else
    {
        answer = a + b + c;
    }
    return answer;
}