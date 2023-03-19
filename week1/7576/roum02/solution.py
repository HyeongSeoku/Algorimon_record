"""
1. 아이디어
- 2중 for => 값 1 && 방문X => BFS
- BFS 돌면서 날짜 +1 => 토마토 자체에 +1씩 해줌


2. 자료구조
- 토마토 상자 int[][]
- queue -> 시간복잡도를 위하여 모듈 deaue 활용
"""

import sys
from collections import deque

read = sys.stdin.readline
m, n = map(int, read().split())
box = [list(map(int, read().split())) for _ in range(n)]

# dy = [0, 1, 0, -1]
# dx = [1, 0, -1, 0]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
queue = deque([])
result = 0


def bfs(y, x):
    queue.append([y, x])
    while queue:
        # 처음 토마토 좌표
        ey, ex = queue.popleft()
        for k in range(4):
            # 다음에 익힐 토마토의 좌표
            ny, nx = ey + dy[k], ex + dx[k]
            print(nx, ny)
            # 좌표(박스) 크기를 넘어가면 안됨 and 해당 좌표 토마토가 익지 않은 상태(0)
            if 0 <= ny < n and 0 <= nx < m and box[ny][nx] == 0:
                print("*****",nx, ny)
                # 토마토를 익힌다 + 날짜 +1 -> 최대값 -1이 정답
                box[ny][nx] = box[ey][ex] + 1
                queue.append([ny, nx])
                print("queue", queue)


for j in range(n):
    for i in range(m):
        if box[j][i] == 1:
            # 맨 처음 토마토가 들어 있는 위치 넣어주기
            bfs(j, i)

for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))

print(result-1)
