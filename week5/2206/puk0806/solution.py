import sys
import copy  

"""
0,0부터 이동하기 진행
벽 하나씩 부수며 이동하기 진행후 가장 작은값 출력

타임에러 ...
벽 제거를 효율적으로 할방법 필요해 보임 ...
"""


def input():
    return sys.stdin.readline().rstrip()


m, n = map(int, input().split())

graph = [list(map(int, input())) for _ in range(m)]
graph[0][0] = -1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(graphInfo):
    queue = []
    queue.append([0,0])

    while queue:
        x,y = queue.pop()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 그래프 밖으로 나갈 때
            if (nx < 0 or nx >= n or ny < 0 or ny >= m) : continue
            # 벽일 경우
            if(graphInfo[ny][nx]==1) : continue
            if(graphInfo[ny][nx]==0 or graphInfo[ny][nx]<graphInfo[y][x]-1):
                graphInfo[ny][nx] = graphInfo[y][x]-1
                queue.append([nx,ny])
    return  graphInfo[m-1][n-1]           


wallList = []

for i in range(m):
    for j in range(n):
        if(graph[i][j]==1):
            wallList.append([j,i])

copyGraph = copy.deepcopy(graph)    # 벽 제거 안한 결과값
result = bfs(copyGraph)

# 벽 하나씩 제거
while wallList:
    rx ,ry = wallList.pop()
    copyGraph = copy.deepcopy(graph)
    copyGraph[ry][rx] = 0
    tempresult = bfs(copyGraph)
    if(result>tempresult):result=tempresult

print(-1 if result==0 else result)    


