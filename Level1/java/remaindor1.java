package Level1;

public class remaindor1 {
    public int solution(int n) {
        int answer = 0;
        for (answer = 1; answer < n; answer++) {
            if (n % answer == 1) {
                return answer;
            }
        }
        return answer;
    }
}
