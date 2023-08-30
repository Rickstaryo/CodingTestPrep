#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list)
{
    int len = num_list.size();
    int tmp = num_list[len - 1] - num_list[len - 2];
    if (tmp > 0)
        num_list.emplace_back(tmp);
    else
        num_list.emplace_back(num_list[len - 1] * 2);
    return num_list;
}