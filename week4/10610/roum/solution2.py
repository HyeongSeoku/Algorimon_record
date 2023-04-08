"""
30

아이디어2
: 30의 배수가 되는 조건을 충족하는 n 중, 최대값 찾기
** 30 배수가 되는 조건: 3의 배수 && 일의 자리가 0
** 3의 배수가 되는 조건: 모든 자리수의 합이 3의 배수
"""

import sys

num_list = list(map(int, sys.stdin.readline().rstrip()))
num_list.sort(reverse=True)
max_number = -1

sum = 0
for i in num_list:
    sum += i

if sum % 3 == 0 and 0 in num_list:
    max_number = int("".join(map(str, num_list)))
    # max_number = reduce(lambda x, y: 10 * x + y, num_list, 0)

print(max_number)
