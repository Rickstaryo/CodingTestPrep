function solution(array, n) {
  var answer = 0;
  for (var a of array) {
    if (n === a) {
      answer += 1;
    }
  }
  return answer;
}
