"""
점프왕 쩰리 ☄️
1) DFS
"""
import sys

read = sys.stdin.readline

n = int(read())
matrix = [list(map(int, read().split(" "))) for _ in range(n)]
visit_matrix = [[0] * n for _ in range(n)]

dx = [1, 0]
dy = [0, 1]


def dfs(y, x, visited_matrix):
    # 범위를 벗어나면 False
    if x >= n or y >= n:
        return False
    # 이미 방문을 했으면 False
    if visited_matrix[y][x] == 1:
        return False
    # 출구에 도달했으면 탈출
    if matrix[y][x] == -1:
        print("HaruHaru")
        exit(0)
    #  방문처리
    visited_matrix[y][x] = 1
    for i in range(2):
        nx = x + dx[i] * matrix[y][x]
        ny = y + dy[i] * matrix[y][x]
        dfs(ny, nx, visited_matrix)
    return True


if dfs(0, 0, visit_matrix):
    print("Hing")
