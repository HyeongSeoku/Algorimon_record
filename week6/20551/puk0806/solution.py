import sys
import bisect

"""
풀이
- 입력 받은 숫자들을 오름차순으로 정렬한다.
- 2진 탐색을 활용하여 가장 먼저 찾은 index를 반환하고 없으면 -1 을 반환
"""

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

numbers = [int(input()) for _ in range(n)]
numbers.sort()
quizs = [int(input()) for _ in range(m)]

for target in quizs:
    result = bisect.bisect_left(numbers, target)
    if(result>=n or numbers[result] !=target):
        print(-1)
    else:
        print(result)
