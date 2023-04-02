'''
    분류 : 그리디
    문제 이름 : 뒤집기
    문제 번호 : 1439
    문제 링크 : https://www.acmicpc.net/problem/1439
'''

import sys
import math


def read():
    return sys.stdin.readline().strip()


text = read()
count = 0

for i in range(len(text) - 1):
    if text[i] != text[i + 1]:
        count += 1

print(math.ceil(count / 2))
