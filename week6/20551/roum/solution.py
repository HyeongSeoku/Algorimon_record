"""
sort 마스터 배지훈의 후계자
=> 시간초과!
"""

import sys

read = sys.stdin.readline
N, M = map(int, read().split(" "))
B = sorted([int(read()) for _ in range(N)])
D = [int(read()) for _ in range(M)]


def find_index(b_list, d_list):
    for d in d_list:
        if d in b_list:
            print(b_list.index(d))
        else:
            print(-1)


find_index(B, D)
