function solution(n, k) {
  // 음식 가격
  const lamb = 12_000;
  const drink = 2_000;
  // 양고기를 10인분 이상 먹었다면
  if (n >= 10) {
    // 10인분 당 음료수 하나 서비스
    k -= (n / 10) << 0;
  }
  return n * lamb + drink * k;
}
