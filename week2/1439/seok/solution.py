'''
    분류 : 그리디
    문제 이름 : 단어수학
    문제 번호 : 1339
    문제 링크 : https://www.acmicpc.net/problem/1339
'''

import sys


def read():
    return sys.stdin.readline().strip()


command_line = int(read())
alpha_dict = {}
word_list = [read() for _ in range(command_line)]
answer = 0

for text in word_list:
    for index in range(len(text)):
        num = 10 ** (len(text) - 1 - index)
        alpha_dict[text[index]] = alpha_dict[text[index]] + \
            num if text[index] in alpha_dict else num

sorted_list = sorted(alpha_dict.values(), reverse=True)

for idx in range(len(sorted_list)):
    answer += int(sorted_list[idx]) * (9 - idx)

print(answer)
