'''
    분류 : BFS/DFS
    문제 이름 : 점프왕 쩰리 (small)
    문제 번호 : 16173
    문제 링크 : https://www.acmicpc.net/problem/16173
'''

# 37:00

import sys
read = sys.stdin.readline

N = int(read().rstrip())

game_map = [list(map(int, read().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
# 초기 좌표
queue = [[0, 0]]

# 아래, 오른
dy = [1, 0]
dx = [0, 1]

while queue:
    y, x = queue.pop()
    jump = game_map[y][x]

    if game_map[y][x] == -1:
        print("HaruHaru")
        exit(0)

    for i in range(2):
        ny = y + dy[i] * jump
        nx = x + dx[i] * jump
        # 해당 부분 런타임 에러 ny < N and nx < N 이어야 함..
        if 0 <= ny <= N and 0 <= nx <= N and visit[ny][nx] == 0:
            visit[ny][nx] = 1
            queue.append([ny, nx])

print("Hing")
