'''
    분류 : Binary sort
    문제 이름 : Sort 마스터 배지훈의 후계자
    문제 번호 : 20551
    문제 링크 : https://www.acmicpc.net/problem/20551
'''


import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())

sort_list = sorted([int(read()) for _ in range(N)])
quiz_list = [int(read()) for _ in range(M)]
mid = 0

for i in quiz_list:
    left, right = 0, len(sort_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sort_list[mid] < i:
            left = mid + 1
        elif sort_list[mid] > i:
            right = mid - 1
        elif sort_list[mid] == i:
            if right == mid:
                break
            right = mid
    if sort_list[mid] == i:
        print(mid)
    else:
        print(-1)
