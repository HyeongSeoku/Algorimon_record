'''
    분류 : 정렬
    문제 이름 : 30
    문제 번호 : 10610
    문제 링크 : https://www.acmicpc.net/problem/10610
'''


'''
끝자리는 무조건 0
없으면 => -1

모든 수들을 더해서 3으로 나눌수 있으면 30의 배수가 될 수 있음
'''

import sys
read = sys.stdin.readline


num_list = list(map(int,read().rstrip()))
num_list.sort(reverse=True)

list_sum = sum(num_list)

result = int("".join(map(str,num_list))) if list_sum%3 == 0 and 0 in num_list else -1

print(result)

