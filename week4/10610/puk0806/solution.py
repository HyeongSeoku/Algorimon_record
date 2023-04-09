"""
풀이 :
- 30의 배수 조건 : 약수들의 배수여야 함.
    - 10의 배수 특징 : 1의 자리가 0이어야함.
    - 3의 배수 특징 각자리의 합이 3의 배수여야함

놓친 부분
- txt은 10^5개의 숫자로 이루어져 있어서 overflow???
    python overflow 없음
- 너무 길어서 타입아웃 예상
    O(n) == O(2n) 똑같아서 이슈없어보임 ..
"""

import heapq
import sys

txt = str(sys.stdin.readline().rstrip())
result = ""
sum = 0
numList = []
zeroFlag = False

for i in range( len(txt)):
    if(txt[i]=='0'): zeroFlag=True
    sum =  int(txt[i])
    heapq.heappush(numList,txt[i])


if(sum%3!=0 | (not zeroFlag)):
    result = -1
else :
    for i in range(len(numList)):
        result = heapq.heappop(numList)+result

print(result)

# 그래도 틀림.... why?

"""
txt = str(sys.stdin.readline().rstrip())
result = ""
sum = 0
obj = {}
keyList = []
zeroFlag = False

for i in range( len(txt)):
    if(txt[i]=='0'): zeroFlag=True
    sum =  (sum+int(txt[i]))%3

    if(txt[i] not in obj):
        obj[txt[i]] = 1
        heapq.heappush(keyList,txt[i]) 
    else:
        obj[txt[i]] +=1
        


if(sum%3!=0 | (not zeroFlag)):
    result = -1
else :
    for i in range(len(keyList)):
        key = heapq.heappop(keyList)
        result = (key*obj[key]) +result

print(result)

"""
    



