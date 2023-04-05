/*
Rick is a fan of logic-based games. However, he is bored of the classic ones, like Sudoku and Mastermind, since he has solved so many of them. Recently he found a new game in which one is given a string with some question marks in it. The objective is to replace all of the question marks with letters (one letter per question mark) in such a way that no letter appears next to another letter of the same kind.

Write a function:

function solution(riddle);


that, given a string  riddle, returns a copy of the string with all of the question marks replaced by lowercase letters (a−z) in such a way that the same letters do not occur next to each other. The result can be any of the possible answers as long as it fulfils the above requirements.

Examples:

1. Given riddle = "ab?ac?", your function might return "abcaca". Some other possible results are "abzacd", "abfacf".

2. Given riddle = "rd?e?wg??", your function might return "rdveawgab".

3. Given riddle = "????????", your function might return "codility".

Write an efficient algorithm for the following assumptions:

the length of the string is within the range [1..100,000];
string riddle consists only of lowercases letters (a − z) or '?';
it is always possible to turn string 'riddle' into a string without two identical consecutive letters.
*/

function solution(riddle) {
  const alph = "abcdefghijklmnopqrstuvwxyz";
  let result = "";
  for (let i = 0; i < riddle.length; i++) {
    if (riddle[i] === "?") {
      const prev = i === 0 ? null : result[i - 1];
      const next = i === riddle.length - 1 ? null : riddle[i + 1];
      let choices = alph;
      if (prev !== null) {
        choices = choices.replace(prev, "");
      }
      if (next !== null) {
        choices = choices.replace(next, "");
      }
      if (choices.length === 0) {
        return "";
      } else {
        result += choices[0];
      }
    } else {
      result += riddle[i];
    }
  }
  return result;
}
