package Level1;

public class desecendingInterger {
  // TimeComplexity is so bad
  // public long solution(long n) {
  // String answer = "";
  // String str = Long.toString(n);

  // int[] arr = new int[str.length()];

  // // long타입의 숫자를 Int배열로 올긴다.
  // for (int i = 0; i < str.length(); i++) {
  // String s = str.substring(i, i + 1);
  // arr[i] = Integer.parseInt(s);
  // }

  // // 내림차순 정렬

  // for (int i = 0; i < str.length(); i++) {
  // for (int j = i + 1; j < str.length(); j++) {
  // if (arr[j] > arr[i]) {
  // int tmp = arr[i];
  // arr[i] = arr[j];
  // arr[j] = tmp;
  // }
  // }
  // }

  // for (int i = 0; i < str.length(); i++) {
  // answer += arr[i];
  // }

  // return Long.parseLong(answer);
  // }
  public long solution(long n) {
    char[] numbers = n.toString().toCharArray();
    String strSort = "";

    if (n <= 0)
      return 0;

    for (int i = 0; i < numbers.length; i++) {
      for (int j = 0; j < i; j++) {
        if (numbers[i] - 48 > numbers[j] - 48) {
          char temp = numbers[i];
          numbers[i] = numbers[j];
          numbers[j] = temp;
        }
      }
    }
    strSort = new String(numbers);

    return Long.parseLong(strSort);
  }
}
