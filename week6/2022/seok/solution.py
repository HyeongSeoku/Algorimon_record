'''
    분류 : Binary sort
    문제 이름 : 사다리
    문제 번호 : 2022
    문제 링크 : https://www.acmicpc.net/problem/2022
'''


import sys
from math import sqrt
read = sys.stdin.readline

x, y, c = map(float, read().rstrip().split())
start, end = 0, min(x, y)


def binary_c(mid):
    h1 = sqrt(x * x - mid * mid)
    h2 = sqrt(y * y - mid * mid)

    return h1 * h2 / (h1 + h2)


result = 0

while end - start > 0.000001:
    mid = (start + end) / 2
    if binary_c(mid) >= c:
        result = mid
        start = mid
    else:
        end = mid

print(round(result, 3))
