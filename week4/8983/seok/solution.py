'''
    분류 : 정렬
    문제 이름 : 사냥꾼
    문제 번호 : 8983
    문제 링크 : https://www.acmicpc.net/problem/8983
'''

'''
|x - a| + b
'''

import sys
read = sys.stdin.readline

M, N, L = map(int, read().rstrip().split(" "))

shooting_zone_list = list(map(int, read().rstrip().split(" ")))
animal_point_list = [tuple(map(int, read().rstrip().split(" ")))
                     for _ in range(N)]
animal_point_list.sort(key=lambda x: x[0])

result = 0

for i in shooting_zone_list:
    for j in animal_point_list[::]:
        if abs(i - j[0]) + j[1] <= L:
            result += 1
            animal_point_list.remove(j)

print(result)
