'''
    분류 : 구현
    문제 이름 : 연구소
    문제 번호 : 12100
    문제 링크 : https://www.acmicpc.net/problem/12100
'''


import sys
import copy
from collections import deque


def bfs_spread_virus():
    virus_queue = deque()
    virus_simulation_map = copy.deepcopy(laboratory)

    for i in range(n):
        for j in range(m):
            if virus_simulation_map[i][j] == 2:
                virus_queue.append((i, j))

        while virus_queue:
            x_coord, y_coord = virus_queue.popleft()

            for k in range(4):
                dx = x_coord + direction[k][0]
                dy = y_coord + direction[k][1]

                if (0 <= dx < n) and (0 <= dy < m):
                    if virus_simulation_map[dx][dy] == 0:
                        virus_simulation_map[dx][dy] = 2
                        virus_queue.append((dx, dy))

    global result
    simulation_count = 0

    for i in range(n):
        for j in range(m):
            if virus_simulation_map[i][j] == 0:
                simulation_count += 1

    result = max(result, simulation_count)


def querantine_wall(wall_count, x, y):
    if (wall_count == 3):
        bfs_spread_virus()
        return
    for i in range(n):
        if i == x:
            k = y
        else:
            k = 0
        for j in range(k, m):
            if laboratory[i][j] == 0:
                laboratory[i][j] = 1
                querantine_wall(wall_count + 1, i, j + 1)
                # 해당 부분을 이해 못해서 오답
                laboratory[i][j] = 0


read = sys.stdin.readline

result = 0
direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]  # 좌우상하

n, m = map(int, (read().split()))
laboratory = [list(map(int, read().split())) for _ in range(n)]

querantine_wall(0, 0, 0)
print(result)
