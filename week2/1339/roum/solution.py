"""
1. 아이디어
: 자리수가 높은 알파벳에 가장 높은 숫자 할당
(1) 두 수의 자리수 비교 -> 길이가 더 긴 str
(2) 더 높은 자리수에 높은 수 할당

2.자료구조
dictionary = {}

"""

import sys

read = sys.stdin.readline

n = int(read())
alphabets = [read().rstrip() for _ in range(n)]
origin_alphabets = alphabets.copy()
numbers = [i for i in range(10)]
# 숫자와 알파벳을 할당할 dictionary
dictionary = {}
# 도출될 값
result = 0


# 각 수의 길이 비교하여 길이가 긴 str 도출
def compare_length(alphabet_list):
    length = 0
    string = ""
    for i in alphabet_list:
        if len(i) > length:
            length = len(i)
            string = i
    return string


# 리스트의 모든 값이 빈 문자열이 될 때 까지 반복: 빈 문자열의 수 == n
while True:
    if alphabets.count("") == n:
        break

    # 가장 높은 자리의 수에 높은 숫자 할당
    max_str = compare_length(alphabets)
    if max_str[0] in dictionary:
        pass
    else:
        dictionary[max_str[0]] = numbers[-1]
        numbers.pop()

    # alphabets 업데이트 하기
    alphabets[alphabets.index(max_str)] = max_str[1:]


# dictionary에 저장된 값 대응
for character in origin_alphabets:
    new_character = ""
    for i in character:
        new_character += str(dictionary[i])
    result += int(new_character)

print(result)