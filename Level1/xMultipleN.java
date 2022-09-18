package Level1;

//https://school.programmers.co.kr/learn/courses/30/lessons/12954
public class xMultipleN {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        long num = x;
        for (int i = 0; i < answer.length; i++) {
            answer[i] = num;
            num += x;
        }
        return answer;
    }
}
