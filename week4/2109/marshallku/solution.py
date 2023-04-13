import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


pay_table = [[] for _ in range(10001)]

for _ in range(int(input())):
    money, day = map(int, input().split())
    pay_table[day].append(money)

heap = []
amount = 0

for t in range(10000, 0, -1):
    for i in pay_table[t]:
        heapq.heappush(heap, -i)
    if heap:
        amount -= heapq.heappop(heap)

print(amount)
