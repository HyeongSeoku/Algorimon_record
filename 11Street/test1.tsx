/*
This is a demo task.

Write a function:

function solution(A);

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
 */

function solution(A) {
  // 주어진 배열에서 양의 정수만 필터링하여 오름차순으로 정렬합니다.
  const filterArr = A.filter((num) => num > 0).sort((a, b) => a - b);

  // 필터링된 배열이 비어있다면, 1을 반환합니다.
  if (filterArr.length === 0) return 1;

  // 필터링된 배열에서 가장 작은 양의 정수를 찾아 반환합니다.
  let result = 1;
  for (let i = 0; i < filterArr.length; i++) {
    if (filterArr[i] > result) break;
    result = filterArr[i] + 1;
  }
  return result;
}
