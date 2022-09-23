package Level1;

public class divisor {
    public int solution(int num) {
        int answer = 0;
        for (int i = 1; i <= num / 2; i++) {
            if (num % i == 0)
                answer += i;
        }
        return answer + num;

    }
}