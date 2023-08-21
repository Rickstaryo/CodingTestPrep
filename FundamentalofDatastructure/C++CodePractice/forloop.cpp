#include <bits/stdc++.h> // --- (1)
using namespace std;     // --- (2)
// Input output  Stream
int main()
{
    vector<int> a = {2, 1, 3};
    do
    {
        for (int i : a)
            cout << i << "|";
        cout << "\n";
    } while (next_permutation(a.begin(), a.end()))
}