"""
풀이 :
- 모든 동물들을 x축이 가까운 사로를 확인하며 사냥 가능한 동물의 수를 파악함

놓친 부분
- x축 좌표가 가까운 사로만 확인하면 됨 (계속 가까운 사로를 찾아줘야함 ...)
- 각 사로별 사냥 가능한 동물확인하는게 나음...

"""


import sys

read = sys.stdin.readline



# 3번째 풀이 9점 ...
"""
m, n, l= map(int, read().split())
shotList = list(map(int,read().split()))
# maxY=0
# maxX=0
# animalList = []
animalDic ={}


for i in range(n):
    tempArr = list(map(int, read().split()))
    # if(maxY<tempArr[1]):maxY=tempArr[1]
    # if(maxX<tempArr[0]):maxX=tempArr[0]
    # animalList.append(tempArr)
    # print("tempArr",tempArr)

    if tempArr[0] in animalDic:
        temp = animalDic[tempArr[0]]
        temp.add(tempArr[1])
        # animalDic[tempArr[0]] = animalDic[tempArr[0]].add(tempArr[1]) 
        animalDic[tempArr[0]] = temp 
    else : animalDic[tempArr[0]]= {tempArr[1]}


# print("animalDic",animalDic)



result = 0
# graph =[[False for col in range(maxX+1)]for row in range(maxY+1)]

# print('animalList',animalList)
# print(maxY)
# print(maxX)
#print(graph)


# for i in range(len(animalList)):
#     graph[animalList[i][1]][animalList[i][0]] = True

for i in range(len(shotList)):
    # print("shotList : ",shotList[i])
    for x in range(shotList[i]-l,shotList[i]+l,1):

        if(x <0 or x not in animalDic) : continue

        for y in range(0,l+1,1):
            #print("x : ",x,"  y :",y ," abs(x-shotList[i])+y : ",abs(x-shotList[i])+y)
            # if(abs(x-shotList[i])+y>l) : continue
     
            if(abs(x-shotList[i])+y<=l and animalDic[x] and y in animalDic[x]):
                animalDic[x] = animalDic[x].remove(y)
                #print('제거@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                #print("x : ",x,"  y :",y ," abs(x-shotList[i])+y : ",abs(x-shotList[i])+y)
                #graph[y][x]=False
                result+=1
print(result)                

"""
                


#2번쨰 풀이 23점....
""""
m, n, l= map(int, read().split())
shotList = list(map(int,read().split()))
maxY=0
maxX=0


animalList = []


for i in range(n):
    tempArr = list(map(int, read().split()))
    if(maxY<tempArr[1]):maxY=tempArr[1]
    if(maxX<tempArr[0]):maxX=tempArr[0]
    animalList.append(tempArr)

result = 0
graph =[[False for col in range(maxX+1)]for row in range(maxY+1)]

# print('animalList',animalList)
# print(maxY)
# print(maxX)
#print(graph)


for i in range(len(animalList)):
    graph[animalList[i][1]][animalList[i][0]] = True

for i in range(len(shotList)):
    #print("shotList : ",shotList[i])
    for x in range(shotList[i]-l,shotList[i]+l,1):

        if(x <0 or maxX<x) : continue

        for y in range(0,l+1,1):
            #print("x : ",x,"  y :",y ," abs(x-shotList[i])+y : ",abs(x-shotList[i])+y)
            if(abs(x-shotList[i])+y>l) : continue
            if(graph[y][x]==True):
                #print('제거@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                #print("x : ",x,"  y :",y ," abs(x-shotList[i])+y : ",abs(x-shotList[i])+y)
                graph[y][x]=False
                result+=1

print(result)                

"""


# 첫풀이 ... 60
"""
m, n, l= map(int, read().split())
shotList = list(map(int,read().split()))

graph = []
for i in range(n):
    graph.append(list(map(int, read().split())))

result = 0

def findNearNum(exList, values):

    return min(exList, key=lambda x:abs(x-values))


for i in range(len(graph)):
    shotPoint  = findNearNum(shotList,graph[i][0])
    if(l>= abs(graph[i][0]-shotPoint)+graph[i][1]):
        result +=1

print(result)
"""






