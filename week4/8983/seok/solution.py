'''
    분류 : 정렬
    문제 이름 : 사냥꾼
    문제 번호 : 8983
    문제 링크 : https://www.acmicpc.net/problem/8983
'''

import sys
read = sys.stdin.readline

M, N, L = map(int, read().rstrip().split(" "))

shooting_zone_list = list(map(int, read().rstrip().split(" ")))
animal_point_list = [list(map(int, read().rstrip().split(" ")))
                     for _ in range(N)]
shooting_zone_list.sort()

result = 0

for x, y in animal_point_list:
    if y > L:
        continue
    min = x + y - L
    max = x - y + L
    start, end = 0, M - 1

    while start <= end:
        mid = (start + end) // 2
        if shooting_zone_list[mid] < min:
            start = mid + 1
        elif shooting_zone_list[mid] > max:
            end = mid - 1
        else:
            result += 1
            break

print(result)
