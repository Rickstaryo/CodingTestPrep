package Level1;

public class GCDLCM {
    public int[] solution(int n, int m) {

        int max = 0;
        int min = 0;
        // for (int i = 1; i <= n && i <= m; i++) { => better option is
        for (int i = 1; i <= Math.max(m, n); i++) {
            if (n % i == 0 && m % i == 0) {
                max = i;
            }
        }
        min = (n * m) / max;

        int[] answer = { max, min };
        return answer;
    }
}
