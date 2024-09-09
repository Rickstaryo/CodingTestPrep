// https://school.programmers.co.kr/learn/courses/30/lessons/120893?language=javascript

// Idea 1 Using isLowerfuntion
// Idea 2 using ASCII code
//

function solution(my_string) {
  let answer = "";
  for (let i of my_string) {
    if (i === i.toUpperCase()) {
      answer += i.toLowerCase();
    } else {
      answer += i.toUpperCase();
    }
  }
  return answer;
}
