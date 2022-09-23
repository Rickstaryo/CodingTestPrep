package Level1;

class addDigits {
    public int solution(int n) {
        int answer = 0;

        while (n != 0) {
            answer += n % 10;
            n /= 10;
        }

        return answer;
    }

}

// better Code
// 왜 리소스를 잡아먹는 코드란 무엇인가??
// public int solution(int number) {
// int answer = 0;
// String[] array = String.valueOf(n).split("");
// for(String s : array){
// answer += Integer.parseInt(s);
// }
// return answer;
// }