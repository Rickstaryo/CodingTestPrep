#include <iostream>

using namespace std;

int main(void)
{
    int n;
    cin >> n;
    if (n % 2 == 0)
    {
        printf("%d is even", n);
    }
    else
    {
        printf("%d is odd", n);
    }
    return 0;
}