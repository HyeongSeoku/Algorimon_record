"""
풀이 :
- 모든 동물들을 x축이 가까운 사로를 확인하며 사냥 가능한 동물의 수를 파악함

놓친 부분
- x축 좌표가 가까운 사로만 확인하면 됨 (계속 가까운 사로를 찾아줘야함 ...)
- 각 사로별 사냥 가능한 동물확인하는게 나음...

"""


import sys

read = sys.stdin.readline

m, n, l= map(int, read().split())
shotList = list(map(int,read().split()))

graph = []
for i in range(n):
    graph.append(list(map(int, read().split())))

result = 0

def findNearNum(exList, values):

    return min(exList, key=lambda x:abs(x-values))



for i in range(len(graph)):
    if(l<graph[i][1]) : continue
    shotPoint  = findNearNum(shotList,graph[i][0])
    if(l>= abs(graph[i][0]-shotPoint)+graph[i][1]):
        result +=1

print(result)




