"""
세 용액
=> 메모리 초과..
"""
import sys
from itertools import combinations
read = sys.stdin.readline

n = int(read())
liquid_list = list(map(int, read().split()))

# 리스트에서 서로 다른 세 조합 구해보기
combination_list = list(combinations(liquid_list, 3))
# 각 조합의 합 중, 절대값의 최소값이 0과 가장 가까운 수
sum_list = [abs(sum(x)) for x in combination_list]
for i in sorted(combination_list[sum_list.index(min(sum_list))]):
  print(i, end=" ")