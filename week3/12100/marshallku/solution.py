"""
Memory usage: 127512 KB
"""
# Always override input
import sys
import copy
from collections import deque
from enum import Enum


def input():
    return sys.stdin.readline().rstrip()


# Solution
WALL_MAX = 3


class State(Enum):
    EMPTY = 0
    WALL = 1
    VIRUS = 2


directions = (
    (0, -1),  # top
    (1, 0),   # right
    (0, 1),   # bottom
    (-1, 0)   # left
)
n, m = map(int, input().split())
map_of_lab = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def is_out(x, y):
    return x < 0 or y < 0 or n <= x or m <= y


def seek():
    global ans
    coords = deque()
    lab = copy.deepcopy(map_of_lab)

    # Add every coords of virus
    for i in range(n):
        for j in range(m):
            if lab[i][j] == State.VIRUS.value:
                coords.append((i, j))

    # Infect every empty cell
    while (coords):
        x, y = coords.popleft()

        for i in range(4):
            dx, dy = directions[i]
            nx = x + dx
            ny = y + dy

            if not is_out(nx, ny) and lab[nx][ny] == State.EMPTY.value:
                lab[nx][ny] = State.VIRUS.value
                coords.append((nx, ny))

    current_ans = 0

    for i in range(n):
        for j in range(m):
            if lab[i][j] == State.EMPTY.value:
                current_ans += 1

    ans = max(current_ans, ans)


# Should I use brute force for sure?
def brute_force(wall_count: int):
    if wall_count == WALL_MAX:
        seek()
        return

    for i in range(n):
        for j in range(m):
            if map_of_lab[i][j] != State.EMPTY.value:
                continue

            # Simulate
            map_of_lab[i][j] = State.WALL.value
            brute_force(wall_count + 1)
            # Restore map
            map_of_lab[i][j] = State.EMPTY.value


brute_force(0)

print(ans)
