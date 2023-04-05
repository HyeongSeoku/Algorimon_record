/*
We call a password secure if it contains no space characters and consists of at least six characters, including at least one digit, one lowercase letter, one uppercase letter and one special character. For the purpose of this task, we will consider just the following characters to be special: !@#$%^&amp;*()_

Write a function:

function solution(S);

that, given a string S of length N, returns true if S is secure (as described above), and returns <tt style="white-space:pre-wrap">false</tt> if it is not secure.

Examples:

1. Given string S = "FooBar123!", the function should return true

2. Given string S = "foobar123!", the function should return false, because there is no uppercase letter.

3. Given string S = "FooBar123", the function should return false, because there is no special character.

4. Given string S = "F0bar! F0bar!", the function should return false, because string S contains a space, which is not a special character.

5. Given string S = "Fo0*", the function should return false, because string S is too short.

Assume that:

the length of string S is within the range [0..100];
S consists only of English lowercase or uppercase letters, digits, spaces and special characters, as indicated above;
spaces won't appear as the first or last character of any password.

In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
*/

// 틀림

function solution(S) {
  const reg =
    /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@#$%^&amp;*()_])[A-Za-z\d@#$%^&amp;*()_]{6,}/;

  return reg.test(S);
}
