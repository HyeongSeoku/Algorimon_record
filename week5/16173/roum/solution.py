"""
점프왕 쩰리 ☄️
1) BFS
"""

import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
matrix = [list(map(int, read().split(" "))) for _ in range(n)]
visit_matrix = [[0] * n for _ in range(n)]

dx = [1, 0]
dy = [0, 1]


def go_jelly(y, x, visited_matrix):
    # 해당 좌표값 queue에 넣고 방문처리
    queue = deque()
    queue.append((y, x))
    visited_matrix[y][x] = 1

    while queue:
        y, x = queue.popleft()
        # 만약 출구에 도달했으면 종료
        if matrix[y][x] == -1:
            return 'HaruHaru'

        # 오른쪽 또는 아래쪽의 좌표
        for i in range(2):
            nx = x + dx[i] * matrix[y][x]
            ny = y + dy[i] * matrix[y][x]
            # matrix 범위 안에 없으면 넘어가기
            if nx >= n or ny >= n:
                continue
            # 이미 방문 했으면 넘어가기
            if visited_matrix[ny][nx] == 1:
                continue
            # 방문을 하지 않았다면
            if visited_matrix[ny][nx] == 0:
                visited_matrix[ny][nx] = 1
                queue.append((ny, nx))
    return 'Hing'


print(go_jelly(0, 0, visit_matrix))
