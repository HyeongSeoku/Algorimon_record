"""
아이디어
: 뭉탱이가 적은 쪽을 뒤집기 == 최소 횟수
1) 연속된 중복 리스트 제거한 새로운 리스트 생성
2) 중복이 제거된 리스트 개수를 비교하여 적은 것이 값이 된다.
"""

import sys

s = sys.stdin.readline().rstrip()
str_list = [i for i in s]


# 중복을 제거한 리스트 생성
def make_deduplication(input_list):
    removed_list = []
    prev = None
    for i in input_list:
        if prev != i:
            removed_list.append(i)
            prev = i
    return removed_list


# hash 형식으로 변경
def make_hash() -> object:
    dictionary = {}
    removed_list = make_deduplication(str_list)
    for key in removed_list:
        if key in dictionary:
            dictionary[key] += 1
        else:
            dictionary[key] = 1
    return dictionary


result_dictionary = make_hash()
if len(result_dictionary.keys()) == 1:
    print(0)
else:
    # 어처피 key는 0과 1밖에 없으므로
    print(min(result_dictionary['0'], result_dictionary['1']))
