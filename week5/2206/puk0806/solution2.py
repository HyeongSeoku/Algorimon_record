import sys
import copy  

"""
0,0부터 이동하기 진행
벽 하나씩 부수며 이동하기 진행후 가장 작은값 출력

- 부순 벽부터 bfs 실행 ...
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


def bfs(graphInfo,sx,sy):
    queue = []
    queue.append([sx,sy])

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

# copyGraph = copy.deepcopy(graph)    # 벽 제거 안한 결과값
result = bfs(graph,0,0)


# 벽 하나씩 제거
while wallList:
    rx ,ry = wallList.pop()
    # print('rx : ',rx,'   ry : ',ry,)
    copyGraph = copy.deepcopy(graph)
    # 벽이 아닌것들중 가장 최단경로 찾기
    maxNum = -1000001  # 1000*1000 
    for i in range(4):
        nx = rx+dx[i]
        ny = ry+dy[i]
        if (nx < 0 or nx >= n or ny < 0 or ny >= m) : continue
        if(copyGraph[ny][nx]==1 or copyGraph[ny][nx]==0) : continue
        if(copyGraph[ny][nx]-1>maxNum):
            maxNum = copyGraph[ny][nx]-1
    if(maxNum==-1000001 ):continue
    copyGraph[ry][rx] = maxNum
    tempresult = bfs(copyGraph,rx,ry)
    if(result>tempresult):result=tempresult

print(-1 if result==0 else result)    


