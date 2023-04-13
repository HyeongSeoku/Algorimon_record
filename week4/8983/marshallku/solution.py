import sys
import bisect


def input():
    return sys.stdin.readline().rstrip()


m, n, l = map(int, input().split())
hunters = sorted(map(int, input().split()))
animals = [tuple(map(int, input().split())) for _ in range(n)]

killed = 0

for x, y in animals:
    hunter_idx = bisect.bisect_left(hunters, x)

    if abs(hunters[hunter_idx] - x) + y <= l:
        killed += 1
    if 0 < hunter_idx and abs(hunters[hunter_idx-1] - x) + y <= l:
        killed += 1

print(killed)
