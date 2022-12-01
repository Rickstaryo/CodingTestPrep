function solution(n) {
  var answer = 0;
  for (var i = 0; i <= n; i++) {
    if (i % 2 == 0) {
      answer += i;
    }
  }
  return answer;
}

// Using for multiple 2
//
function solution(n) {
  var answer = 0;
  for (var i = 0; i <= n; i += 2) {
    answer += i;
  }
  return answer;
}
