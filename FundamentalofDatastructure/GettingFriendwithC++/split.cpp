#include <bits/stdc++.h>
using namespace std;

vector<string> split(string input, string delimiter)
{
    // Result
    vector<string> ret;
    long long pos = 0;
    string token = "";
    while ((pos = input.find(delimiter)) != string::npos)
    {
        token = input.substr(0, pos);
        ret.push_back(token);
        input.erase(0, pos + delimiter.size());
    }
    ret.push_back(input);
    return ret;
}

int main()
{
    string s = "안녕하세요    큰돌이는    킹갓제너럴    천재입니다    정말이에요!", d = " ";
    vector<string> a = split(s, d);
    for (string b : a)
        cout << b << "\n";
}