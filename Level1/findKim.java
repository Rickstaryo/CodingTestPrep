package Level1;

public class findKim {

    public String solution(String[] seoul) {
        int x = 0;
        /*
         * for(x=0;x<seoul.length;x++) {
         * if(seoul[x].equals("Kim"))
         * break;
         * }
         */

        for (String name : seoul) {
            if (name.equals("Kim"))
                break;
            x++;
        }
        return "김서방은 " + x + "에 있다";
    }
}
