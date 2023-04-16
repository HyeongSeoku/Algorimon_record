import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
matrix = [list(map(lambda x: [int(x), False], input().split()))
          for _ in range(n)]
directions = (
    (1, 0),   # right
    (0, 1),   # bottom
)
moves = deque([(0, 0)])


def is_out(x, y):
    return x < 0 or y < 0 or n <= x or n <= y


def main():
    while moves:
        x, y = moves.popleft()
        current_position, visited = matrix[x][y]

        if current_position == -1:
            return True

        for dx, dy in directions:
            nx, ny = x + dx * current_position, y + dy * current_position

            if not is_out(nx, ny) and not visited:
                matrix[x][y][1] = True
                moves.append([nx, ny])

    return False


print('HaruHaru' if main() else 'Hing')
