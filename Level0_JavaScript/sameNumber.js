function solution(array, n) {
  var answer = 0;
  for (var a of array) {
    if (n === a) {
      answer += 1;
    }
  }
  return answer;
}


function solution(array, n) {
    return array.filter(f=>f===n).length;
}