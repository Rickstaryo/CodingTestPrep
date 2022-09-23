package Level1;

public class StringToInterger {

    public int Idiotsolution(String s) {
        return Integer.parseInt(s);
    }

    public int realSolution(String str) {
        int result = 0;
        int i = 0;
        // Check positive and Negative
        boolean negative = false;
        if (str.charAt(0) == '-') {
            negative = true;
            i++;
        } else if (str.charAt(0) == '+')
            i++;
        while (i < str.length() && str.charAt(i) >= '0' && str.charAt(i) <= '9') {
            result = result * 10 + (str.charAt(i) - '0');
            i++;
        }

        return result;
    }

}
