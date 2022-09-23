package Level1;

import java.util.Arrays;

public class StringDescade {
    public String solution(String str) {
        char[] chars = str.toCharArray();
        char temp = ' ';

        for (int i = 0; i < str.length(); i++) {
            for (int j = 0; j < str.length() - 1; j++) {
                if (chars[j] < chars[j + 1]) {
                    temp = chars[j];
                    chars[j] = chars[j + 1];
                    chars[j + 1] = temp;
                }
            }
        }
        str = new String(chars, 0, chars.length);
        return str;
    }
}
