#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    while (n>1){
        if (n%2==0){
            answer.push_back(n);
            n=n/2;
        }
        else{
            answer.push_back(n);
            n=n*3+1;
        }
            
    }
    answer.push_back(1);
    return answer;
}