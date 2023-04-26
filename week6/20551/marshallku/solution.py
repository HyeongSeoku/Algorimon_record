import sys


def input():
    return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])
idx_map = {arr[i]: i for i in range(n) if i == 0 or arr[i] != arr[i-1]}


for _ in range(m):
    print(idx_map.get(int(input()), -1))
