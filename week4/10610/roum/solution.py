"""
30
아이디어

1. 수의 순열 찾기
2. 해당 수의 순열의 조합 중 30의 배수 찾기
2-1. 배수가 없다면 -1출력
2-2. 배수가 있다면 배수 중 가장 큰 값 출력

"""

import sys
from itertools import permutations

num_list = list(sys.stdin.readline().rstrip())
perm_list = permutations(num_list, len(num_list))

max_number = -1

# 순열의 조합 중 30의 배수 찾기
for i in perm_list:
    number = int(''.join(i))
    if number % 30 == 0:
        max_number = max(max_number, number)

print(max_number)
