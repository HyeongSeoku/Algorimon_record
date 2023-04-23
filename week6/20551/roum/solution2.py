"""
sort 마스터 배지훈의 후계자
=> 이진탐색 + 중복값이 있을 경우의 case 추가 필요
"""

import sys

read = sys.stdin.readline
N, M = map(int, read().split(" "))
B = sorted([int(read()) for _ in range(N)])
D = [int(read()) for _ in range(M)]


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 1) 중간값이 타겟값일 경우 => 중복값이 있을 경우 재귀 실행
    if array[mid] == target:
        if end == mid:
            return mid
        else:
            return binary_search(array, target, start, mid)
    # 2) 중간값이 타겟값보다 클 경우
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 3) 중간값이 타겟값보다 작을 경우
    else:
        return binary_search(array, target, mid + 1, end)


for d in D:
    result = binary_search(B, d, 0, N - 1)
    result = -1 if not isinstance(result, int) else result
    print(result)
