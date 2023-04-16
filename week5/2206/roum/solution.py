"""
벽 부수고 이동하기...
1) bfs 최단거리 함수 실행
2) 1로 바꿔보기
3) min((1),(2)) => 시간이 너무 오래걸릴

"""

import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split(" "))
matrix = [list(map(int, read().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    is_broken = 0

    while queue:
        y, x = queue.popleft()
        # 맨 끝 점에 도달하면 이동거리 출력
        if y == n - 1 and x == m - 1:
            return visited[y][x]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 조건에 충족하지 않는 경우 넘어감
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            # 다음 이동할 곳이 벽이 아니고 한 번도 방문하지 않은 경우
            if matrix[ny][nx] == 0 and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))
            # 다음 이동할 곳이 벽이고 벽을 아직 파괴하지 않은 경우
            if matrix[ny][nx] == 1 and is_broken == 0:
                is_broken = 1
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))
                print(queue)
    return -1


print(bfs(0, 0))
