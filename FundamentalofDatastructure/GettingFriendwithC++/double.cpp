#include <string>
#include <vector>
using namespace std;

int solution(vector<int> num_list)
{
    int sum = 0, mul = 1;
    for (const auto &a : num_list)
    {
        sum += a;
        mul *= a;
    }
    return mul < sum * sum ? 1 : 0;
}