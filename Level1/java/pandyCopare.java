package Level1;

public class pandyCopare {
    boolean solution(String s) {

        int pCounter = 0;
        int yCounter = 0;
        String[] arr = s.toUpperCase().split("");
        for (int i = 0; i < arr.length; i++) {
            if ("P".equals(arr[i])) {
                pCounter++;
            } else if ("Y".equals(arr[i])) {
                yCounter++;
            }
        }

        if (pCounter != yCounter) {
            return false;
        }
        return true;
    }
    /*
     * 
     * boolean solution(String s) {
     * s = s.toLowerCase();
     * int count = 0;
     * 
     * for (int i = 0; i < s.length(); i++) {
     * 
     * if (s.charAt(i) == 'p')
     * count++;
     * else if (s.charAt(i) == 'y')
     * count--;
     * }
     * 
     * if (count == 0)
     * return true;
     * else
     * return false;
     * }
     */
}
