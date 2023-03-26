"""
1. 아이디어(2)
: 각 자리수의 가중치를 계산
"""

import sys

read = sys.stdin.readline

n = int(read())
alphabets = [read().rstrip() for _ in range(n)]
sum_result = 0

# 알파벳의 가중치를 계산
dictionary = {}
for word in alphabets:
    for i in range(len(word)):
        if word[i] not in dictionary:
            dictionary[word[i]] = pow(10, len(word) - i - 1)
        else:
            dictionary[word[i]] += pow(10, len(word) - i - 1)

# 가중치의 내림차순
sorted_dictionary = sorted(dictionary.values(), reverse=True)

num = 9
for i in range(len(sorted_dictionary)):
    sum_result += sorted_dictionary[i] * num
    num -= 1

print(sum_result)
