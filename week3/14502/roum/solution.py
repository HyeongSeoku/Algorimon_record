"""
연구소

아이디어
1) 벽을 세울 수 있는 모든 조합 찾기
2) 바이러스 전파해보기 (dfs)
3) 가장 넓은 안전지대 출력

"""

import sys
import copy

read = sys.stdin.readline

n, m = map(int, read().split(" "))
lab = [list(map(int, read().split(" "))) for _ in range(n)]

# 오 왼 위 아래
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

# 안전 영역 리스트
safe_list = []


def virus_spread():
    lab_list = copy.deepcopy(lab)
    # 바이러스가 있을 경우 해당 좌표를 stack 에 넣기
    virus_stack = [(y, x) for y in range(n) for x in range(m) if lab_list[y][x] == 2]

    while virus_stack:
        y, x = virus_stack.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and lab_list[ny][nx] == 0:
                lab_list[ny][nx] = 2
                virus_stack.append((ny, nx))
    return lab_list


# 안전 영역 개수 구하기
def count_safe_zone(lab_list):
    safe_zone = 0
    for j in lab_list:
        safe_zone += j.count(0)

    return safe_zone


# 벽 세우기 함수
def make_wall(lab_list, wall_count):
    if wall_count == 0:
        lab_list_case = virus_spread()
        safe_list.append(count_safe_zone(lab_list_case))
        return
    for y in range(n):
        for x in range(m):
            if lab_list[y][x] == 0:
                lab_list[y][x] = 1
                make_wall(lab_list, wall_count - 1)
                # 새로운 경우의 수를 위한 초기화
                lab_list[y][x] = 0


make_wall(lab, 3)
print(max(safe_list))
