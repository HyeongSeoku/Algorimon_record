"""
시간초과 -> 3차원 리스트
"""

import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split(" "))
matrix = [list(map(int, read().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))
    visited[x][y][z] = 1

    while queue:
        x, y, z = queue.popleft()
        # 맨 끝 점에 도달하면 이동거리 출력
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 조건에 충족하지 않는 경우 넘어감
            if ny < 0 or ny >= m or nx < 0 or nx >= n:
                continue
            # 다음 이동할 곳이 벽이고, 벽을 아직 파괴하지 않은 경우
            if matrix[nx][ny] == 1 and z == 0:
                # 벽을 파괴하고 간다
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))
                print("파괴:", nx, ny)
            # 다음 이동할 곳이 벽이 아니고 한 번도 방문하지 않은 경우
            elif matrix[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
                print("이동:", nx, ny)
    return -1


print(bfs(0, 0, 0))
