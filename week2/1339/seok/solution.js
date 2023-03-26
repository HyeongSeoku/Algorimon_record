/*
    분류 : 그리디
    문제 이름 : 단어수학
    문제 번호 : 1339
    문제 링크 : https://www.acmicpc.net/problem/1339
*/

const fs = require("fs");

// 백준 제출시 주석 제거
// const readFileSyncAddress = "/dev/stdin"

// 테스트시 주석 제거
const readFileSyncAddress = "example.txt";

const input = fs.readFileSync(readFileSyncAddress).toString().split("\n");
const [commandLine, ...wordList] = input;
const alphaObj = {};

wordList.forEach((word) => {
  word.split("").forEach((alphabet, index) => {
    alphaObj.hasOwnProperty(alphabet)
      ? (alphaObj[alphabet] += 10 ** (word.length - 1 - index))
      : (alphaObj[alphabet] = 10 ** (word.length - 1 - index));
  });
});

const answer = Object.values(alphaObj)
  .sort((a, b) => b - a)
  .reduce((acc, cur, idx) => {
    return acc + cur * (9 - idx);
  }, 0);

console.log(answer);
