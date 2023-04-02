"""
연구소
-> 기본적인 아이디어는 동일하나, 조합 이용한 풀이

아이디어
1) 벽을 세울 수 있는 모든 조합 찾기
2) 바이러스 전파해보기 (dfs)
3) 가장 넓은 안전지대 출력

"""

import sys
import copy
from itertools import combinations

read = sys.stdin.readline

n, m = map(int, read().split(" "))
lab = [list(map(int, read().split(" "))) for _ in range(n)]

# 오 왼 위 아래
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

# 안전 영역 리스트
safe_list = []
# 벽을 세울 수 있는 좌표 리스트
empty_list = [(y, x) for y in range(n) for x in range(m) if lab[y][x] == 0]

max_result = 0


def make_wall(wall_count):
    global max_result
    for combination in combinations(empty_list, wall_count):
        lab_list = copy.deepcopy(lab)
        for y, x in combination:
            lab_list[y][x] = 1
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
        safe_zone = 0
        for j in lab_list:
            safe_zone += j.count(0)

        max_result = max(max_result, safe_zone)
    print(max_result)


make_wall(3)