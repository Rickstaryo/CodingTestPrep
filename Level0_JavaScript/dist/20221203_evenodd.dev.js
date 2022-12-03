"use strict";

// function solution(num_list) {
//   var answer = [];
//   var odd = 0;
//   var even = 0;
//   for (var i = 0; i < num_list.length; i++) {
//     if (num_list[i] % 2 == 0) {
//       even += 1;
//     } else if (num_list[i] % 2 != 0) {
//       odd += 1;
//     }
//   }
//   answer.push(even, odd);
//   return answer;
// }
var fruits = ["apple", "banana", "grapes", "mango", "orange"];
/**
 * Filter array items based on search criteria (query)
 */

function filterItems(arr, query) {
  return arr.filter(function (el) {
    return el.toLowerCase().includes(query.toLowerCase());
  });
}

console.log(filterItems(fruits, "ap")); // ['apple', 'grapes']

console.log(filterItems(fruits, "an")); // ['banana', 'mango', 'orange']