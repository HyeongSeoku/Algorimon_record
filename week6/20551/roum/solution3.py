"""
sort 마스터 배지훈의 후계자
=> 순차탐색
=> 시간초과
"""

import sys

read = sys.stdin.readline
N, M = map(int, read().split(" "))
B = sorted([int(read()) for _ in range(N)])
D = [int(read()) for _ in range(M)]


def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i


for d in D:
    result = sequential_search(N, d, B)
    result = -1 if not isinstance(result, int) else result
    print(result)
