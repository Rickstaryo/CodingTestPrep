package Level1;

import java.util.*;

public class budget {
    public int solution(int[] d, int budget) {
        // https://school.programmers.co.kr/learn/courses/30/lessons/12982
        int answer = 0;
        Arrays.sort(d);
        for (int i = 0; i < d.length; i++) {
            budget -= d[i];
            if (budget < 0)
                break;
            answer++;
        }
        return answer;
    }
}
