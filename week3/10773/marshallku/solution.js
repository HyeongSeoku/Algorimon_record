const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");
const answerList = [];

for (let i = 1; i <= +input[0]; ++i) {
    const num = input[i];

    if (num === "0") {
        answerList.pop();
    } else {
        answerList.push(num);
    }
}

let result = 0;

for (let i = 0, len = answerList.length; i < len; ++i) {
    result += +answerList[i];
}

console.log(result);
