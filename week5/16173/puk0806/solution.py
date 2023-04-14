"""
풀이
- 0,0에서 시작해서 해당 이동할수 거리 만큼 우측과 아래쪽을 확인하면 DFS를 활용함

주의사항
- 이동거리가 0인것도 있음
"""

import sys

read = sys.stdin.readline

n = int(read())
graph = [list(map(int, read().split())) for _ in range(n)]

dx = [1, 0]
dy = [0, 1]

result = "Hing"
stack = []

stack.append([0,0])

while stack:
    x,y =stack.pop()
    for i in range(2):
        nx = x+ dx[i]*graph[x][y]
        ny = y + dy[i]*graph[x][y]
        if (nx < 0 or nx >= n or ny < 0 or ny >= n) :
            continue
        if(graph[nx][ny]==0):continue

        if(graph[nx][ny]==-1):
            result="HaruHaru"
            break
        else:
            stack.append([nx,ny])
        

print(result)

