# 순회강연

## Failed

```py
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
```

문제를 잘못 읽고 n일에 오라는 얘긴 줄 알고, 도대체 이게 왜 골드인지 의문을 갖고 막코딩을 한 뒤 제출했는데 오답입니다.\
다시 차분히 문제를 읽어보니 n일 안에 와야하는 거였습니다.

## Description

heapq 이용하여 풀이할 수 있습니다.
