package Level1;

public class palindromeHighSpeed {
    public int[] solution(long n) {
        String str = String.valueOf(n);
        int[] answer = {};

        // Data set

        // Why this code doesn't use the + opereator ??
        // Because when you just add a String then it's take off a lot of time
        // https://onlyfor-me-blog.tistory.com/317
        // https://www.codejava.net/java-core/the-java-language/why-use-stringbuffer-and-stringbuilder-in-java
        StringBuilder sb = new StringBuilder(str);
        sb = sb.reverse();

        String[] arr = sb.toString().split("");
        answer = new int[sb.length()];
        for (int i = 0; i < sb.length(); i++) {
            answer[i] = Integer.parseInt(arr[i]);
        }
        return answer;
    }
}
