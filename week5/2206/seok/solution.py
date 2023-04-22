'''
    분류 : BFS/DFS
    문제 이름 : 벽 부수고 이동하기
    문제 번호 : 2206
    문제 링크 : https://www.acmicpc.net/problem/2206
'''

'''
    최단 경로 = BFS
    시작하는 칸과 끝나는 칸도 포함해서 세야함
'''

import sys
from collections import deque
read = sys.stdin.readline

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


N, M = map(int, read().rstrip().split())

map = [list(map(int, read().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

queue = deque()
queue.append((0, 0, 0))

while queue:
    a, b, c = queue.popleft()

    if a == N - 1 and b == M - 1:
        print(visited[a][b][c])
        exit(0)

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        # 맵 벗어날 경우
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if map[nx][ny] == 1 and c == 0:
            visited[nx][ny][1] = visited[a][b][0] + 1
            queue.append((nx, ny, 1))
        elif map[nx][ny] == 0 and visited[nx][ny][c] == 0:
            visited[nx][ny][c] = visited[a][b][c] + 1
            queue.append((nx, ny, c))

print(-1)
