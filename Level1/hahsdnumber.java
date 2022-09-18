package Level1;

public class hahsdnumber {
    public boolean solution(int x) {
        int num = x;
        int hashad = 0;
        while (num >= 1) {
            hashad += num % 10;
            num /= 10;
        }

        return x % hashad == 0 ? true : false;

    }
}
