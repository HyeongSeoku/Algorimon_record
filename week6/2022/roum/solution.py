"""
사다리..
"""

import sys
from math import sqrt
read = sys.stdin.readline

x, y, c = map(float, read().split(" "))


def get_c(x, y, l):
    h1 = sqrt(x*x-l*l)
    h2 = sqrt(y*y-l*l)
    return (h1*h2)/(h1+h2)


start, end = 0, min(x, y)

while end-start > 0.000001:
    mid = (start+end) / 2
    # mid값이 c보다 더 클 경우
    if get_c(x, y, mid) >= c:
        start = mid
    # mid값이 c보다 더 작을 경우
    else:
        end = mid

# mid == c일 경우는 그냥 답이다.
print(start)
