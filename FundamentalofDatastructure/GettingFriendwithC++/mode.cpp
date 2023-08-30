#include <string>
#include <vector>

using namespace std;

string solution(string code)
{
    string answer = "";
    string ret;
    int mode = 0;

    int len = code.length();

    for (int i = 0; i < len; ++i)
    {
        if (mode == 0)
        {
            if (code[i] != '1')
            {
                if (i % 2 == 0)
                {
                    ret += code[i];
                }
            }
            else
            {
                mode = 1;
            }
        }

        else if (mode == 1)
        {
            if (code[i] != '1')
            {
                if (i % 2 != 0)
                {
                    ret += code[i];
                }
            }
            else
            {
                mode = 0;
            }
        }
    }

    if (ret.empty())
        return "EMPTY";
    else
        return ret;
}