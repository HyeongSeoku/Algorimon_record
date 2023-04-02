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

for (const num of list) {
  if (num === 0) answerList.pop();
  else answerList.push(num);
}

console.log(answerList.reduce((acc, cur) => (acc += cur), 0));
