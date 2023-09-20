#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solution(string my_string, vector<vector<int>> queries)
{
    string answer = my_string;
    for (auto &query : queries)
    {
        reverse(answer.begin() + query[0], answer.begin() + query[1] + 1);
    }
    return answer;
}