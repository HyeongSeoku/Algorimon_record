import math
import sys

str = str(sys.stdin.readline().rstrip())

result =0

for i in range(1,len(str),1):
    if(str[i-1]!=str[i]): result +=1

print(math.ceil(result/2))
