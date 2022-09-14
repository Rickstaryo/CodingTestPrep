package Level1;

public class divisor {
    public int solution(int n) {
        int answer = 0;
        for (int i = 1; i < n + 1; i++) {
            if (n % i == 0) {
                answer += i;
            }
        }
        return answer;
    }
}

// Better Code
// public int solution(int n) {
// int answer = 0;
// for (int i = 1; i < n/2; i++) {
// if (n % i == 0) {
// answer += i;
// }
// }
// return answer;
// }