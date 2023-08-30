#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list)
{
    int answer = 0;
    string e = "";
    string o = "";
    for (int i = 0; i < num_list.size(); i++)
    {
        string a = to_string(num_list[i]);
        if (num_list[i] % 2 == 0)
        {
            e += a;
        }
        else
        {
            o += a;
        }
    }
    return stoi(o) + stoi(e);
}