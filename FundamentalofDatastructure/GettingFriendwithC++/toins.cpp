#include <string>
#include <vector>

using namespace std;

int solution(int a, int b)
{
    int answer = 0;
    string apb = to_string(a) + to_string(b);
    int axb = a * b * 2;
    answer = max(axb, stoi(apb));
    return answer;
}