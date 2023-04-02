'''
    분류 : 구현
    문제 이름 : 제로
    문제 번호 : 10773
    문제 링크 : https://www.acmicpc.net/problem/10773
'''


'''
    수를 하나씩 입력받고,
    0이 있으면 가장 최근에 들어온 수 pop
'''

import sys
read = sys.stdin.readline

K = int(read())
list = []

for i in range(K):
    num = int(read())
    list.append(num) if num != 0 else list.pop()

print(sum(list))
