import sys
import copy  
"""
너무 느림... 개선 필요 
"""

def input():
    return sys.stdin.readline().rstrip()

n, m, oli = map(int, input().split())

graph = [[0 for i in range(n+1)]]

for i  in range(n):
    graph += [list(map(int, ("0 "+input()).split(" ")))]

cy,cx = map(int, input().split())

popleInfo = [list(map(int, input().split(" "))) for _ in range(m)]


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(graphInfo,sy,sx):
    queue = []
    queue.append([sy,sx])

    while queue:
        y,x = queue.pop()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 그래프 밖으로 나갈 때
            if (nx < 1 or nx > n or ny < 1 or ny > n) : continue
            # 벽일 경우
            if(graphInfo[ny][nx]==1) : continue
            if(graphInfo[ny][nx]==0 or graphInfo[ny][nx]<graphInfo[y][x]-1):
                # print('변화')
                graphInfo[ny][nx] = graphInfo[y][x]-1
                queue.append([ny,nx])

def endFail():
    print(-1)
    exit(0)

while popleInfo:
    copyGraph = copy.deepcopy(graph)
    dfs(copyGraph,cy,cx)

    distance = -500 # 최대 -거리 21*21
    tempIndex = -1
    tempEndY =0
    tempEndX =0

    # 가장 가까운 사람 찾기
    for i in range(len(popleInfo)):
        sy,sx,ey,ex = popleInfo[i]
        # 벽인경우는 없겠지...
        # 갈수 없는 경우
        if(copyGraph[sy][sx]==0 or copyGraph[ey][ex]==0) : endFail()

        #사람 태우는 우선순위 조건
        if(copyGraph[sy][sx]>distance or (copyGraph[sy][sx]==distance and (sy<cy or (sy==cy and sx<cx)   )  )):
            tempIndex = i
            cy = sy
            cx = sx
            tempEndY =ey
            tempEndX  = ex
            distance = copyGraph[sy][sx]



    oli += copyGraph[cy][cx]
    # 연료 부족 (태우러 갈때)
    if(oli <0) : endFail()
    popleInfo.pop(tempIndex)
    
    
    copyGraph = copy.deepcopy(graph)
    dfs(copyGraph,cy,cx)

    cy = tempEndY
    cx = tempEndX

    # 연료 부족 (목적지)
    if(oli + copyGraph[cy][cx]<0) : endFail()

    oli -= copyGraph[cy][cx]

print(oli)









            

        







