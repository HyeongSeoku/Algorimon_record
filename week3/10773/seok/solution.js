/*
    분류 : 구현
    문제 이름 : 제로
    문제 번호 : 10773
    문제 링크 : https://www.acmicpc.net/problem/10773
*/

const fs = require("fs");

// 백준 제출시 주석 제거
// const readFileSyncAddress = "/dev/stdin"

// 테스트시 주석 제거
const readFileSyncAddress = "example.txt";
const input = fs
  .readFileSync(readFileSyncAddress)
  .toString()
  .split("\n")
  .map((item) => +item);

const [K, ...list] = input;
const answerList = [];

for (let i = 0; i < K; ++i) {
  if (list[i] === 0) {
    answerList.pop();
  } else answerList.push(list[i]);
}

let answer = 0;
for (let i = 0, len = answerList.length; i < len; ++i) {
  answer += answerList[i];
}

console.log(answer);
