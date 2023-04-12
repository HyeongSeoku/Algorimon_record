"""
순회강연

1) 우선순위 큐를 day 값으로 정렬
2) for 돌면서 day값과 queue길이 비교해서 pay값 작은 것 빼기
3) queue의 합계

"""
import sys
import heapq

read = sys.stdin.readline

n = int(read())
pay_day_list = [list(map(int, read().split(" "))) for _ in range(n)]
q = []

# day 순서로 정렬
pay_day_list.sort(key=lambda x : x[1])

for pay, day in pay_day_list:
    heapq.heappush(q, pay)
    # 만약 day값이 q의 길이보다 작으면 == day순으로 정렬했으므로 길이에서 벗어나면 날짜가 오바된 것이므로
    if day < len(q):
        # pay값이 가장 작은 값을 없애준다
        heapq.heappop(q)

print(sum(q))
