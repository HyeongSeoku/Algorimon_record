import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
matrix = [[list(map(int, input().split())) + [0, 0]
           for _ in range(m)] for _ in range(n)]
directions = (
    (0, -1),  # top
    (1, 0),   # right
    (0, 1),   # bottom
    (-1, 0)   # left
)


def is_out(x, y):
    return x < 0 or y < 0 or n <= x or m <= y


def main():
    moves = deque([(0, 0, 1)])
    matrix[0][0][2] = 1

    while moves:
        x, y, b = moves.popleft()

        if x == n - 1 and y == m - 1:
            return matrix[x][y][b + 1]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if is_out(nx, ny):
                continue

            if matrix[nx][ny][0] == 0 and matrix[nx][ny][b + 1] == 0:
                moves.append((nx, ny, b))
                matrix[nx][ny][b + 1] = matrix[x][y][b + 1] + 1

            if matrix[nx][ny][0] == b == 1:
                moves.append((nx, ny, b - 1))
                matrix[nx][ny][b] = matrix[x][y][b + 1] + 1

    return -1


print(main())
