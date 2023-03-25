"""
1. 아이디어
: 뭉탱이가 적은 쪽을 뒤집기 == 최소 횟수
처음부터 돌면서 0,1의 뭉탱이를 찾는다.

연속된 값을 다 더한다
리스트의 길이 - 0의 뭉탱이, 0의 길이 비교

2. 시간복잡도 O(n)

3. 자료구조
n = 전체 str의 길이의 수
zero_zone = 0 뭉탱이의 수
one_zone = 1 뭉탱이의 수
"""

import sys

s = sys.stdin.readline().rstrip()
zero_zone = 0
one_zone = 0
#
# for i in range(len(s)):
#     if s[-i] != s[-(i + 1)]:
#         if s[i] == "0":
#             zero_zone += 1
#         else:
#             one_zone += 1
#
# result = min(zero_zone, one_zone)
# print(result)

# 방법1: 0, 1 zone 개수 비교
str_list = [i for i in s]
for i in str_list:
    str_list.pop()
    print(i, str_list[len(str_list)-1], str_list)
    # 맨 마지막 값과 그 앞에 있는 값 비교
    if str_list[len(str_list)-1] != i:
        if i == '0':
            zero_zone += 1
        else:
            one_zone += 1
    # 리스트의 마지막일 경우
    # print(str_list, zero_zone, one_zone)