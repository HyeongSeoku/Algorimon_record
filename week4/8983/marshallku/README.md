# 사냥꾼

## Description

사대를 정렬하고, 동물을 사격할 수 있는 사정거리 내에 사대가 있는지 검색하면 됩니다.

```py
import sys


def input():
    return sys.stdin.readline().rstrip()


m, n, l = map(int, sys.stdin.readline().rstrip().split())
hunters = sorted(map(int, sys.stdin.readline().rstrip().split()))
animals = [map(int, sys.stdin.readline().rstrip().split()) for _ in range(n)]

killed = 0
for x, y in animals:
    if any(abs(x-hunter) + y <= l for hunter in hunters):
        killed += 1

print(killed)
```

위와 같이 일반적인 풀이로는 5번을 통과할 수 없어, binary search를 이용해야 합니다.\
binary search가 다른 x 좌표를 같는 사대를 선택한 채로 끝나는 케이스를 대비해 전후 사대도 체크하면 통과할 수 있습니다.
