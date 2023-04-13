import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
calendar = {}

for _ in range(n):
    money, day = map(int, input().split())

    if calendar[day]:
        calendar[day].append(money)
    else:
        calendar[day] = [money]

amount = 0
for x in calendar:
    amount += max(x)

print(amount)
