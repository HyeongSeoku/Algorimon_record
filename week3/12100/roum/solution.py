"""
2048
아이디어
1) 가장 큰 수 찾기
2) 겹칠 수 있다면 겹치기, 안되면 그 다음 큰 수 찾기(1로 이동)
3) 겹치기 -> 숫자가 있는 곳 까지 전진(0이면 계속 이동) / 빈 자리 0으로 채우기

(수정)
1) 동서남북 모두 dfs 돌리기 -> 최대값 출력
2) 이동시
- 비어있으면 옮기기
- 같으면: 합치기
- 다른 값이면 옆에 붙이기

"""
import sys, copy

read = sys.stdin.readline
n = int(read())
board = [list(map(int, read().split(" "))) for _ in range(n)]
answer = 0


def left(board_copy):
    for y in range(n):
        cursor = 0
        for x in range(1, n):
            if board_copy[y][x] != 0:
                temp = board_copy[y][x]
                board_copy[y][x] = 0

                # 비어있으면 옮기기
                if board_copy[y][cursor] == 0:
                    board_copy[y][cursor] = temp
                # 같으면 합치기
                elif board_copy[y][cursor] == temp:
                    board_copy[y][cursor] *= 2
                    cursor += 1
                # 다른 값이면 옆에 붙이기
                else:
                    cursor += 1
                    board_copy[y][cursor] = temp
    return board_copy


def right(board_copy):
    for y in range(n):
        # 오른쪽으로 가야 하기 때문
        cursor = n - 1
        for x in range(n - 1, -1, -1):
            if board_copy[y][x] != 0:
                temp = board_copy[y][x]
                board_copy[y][x] = 0

                if board_copy[y][cursor] == 0:
                    board_copy[y][cursor] = temp
                elif board_copy[y][cursor] == temp:
                    board_copy[y][cursor] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    board_copy[y][cursor] = temp
    return board_copy


def up(board_copy):
    for y in range(n):
        cursor = 0
        for x in range(n):
            if board_copy[x][y] != 0:
                temp = board_copy[x][y]
                board_copy[x][y] = 0

                if board_copy[cursor][y] == 0:
                    board_copy[cursor][y] = temp
                elif board_copy[cursor][y] == temp:
                    board_copy[cursor][y] *= 2
                    cursor += 1
                else:
                    cursor += 1
                    board_copy[cursor][y] = temp
    return board_copy


def down(board_copy):
    for y in range(n):
        cursor = n - 1
        for x in range(x):
            if board_copy[x][y] != 0:
                temp = board_copy[x][y]
                board_copy[x][y] = 0

                if board_copy[cursor][y] == 0:
                    board_copy[cursor][y] = temp
                elif board_copy[cursor][y] == temp:
                    board_copy[cursor][y] *= 2
                else:
                    cursor -= 1
                    board_copy[cursor][y] = temp
    return board_copy


def dfs(num, board_list):
    global answer

    if n == 5:
        for y in range(n):
            for x in range(n):
                if board_list[y][x] > answer:
                    answer = board_list[y][x]
        return

    for i in range(4):
        board_copy = copy.deepcopy(board_list)
        if i == 0:
            dfs(num + 1, left(board_copy))
        elif i == 1:
            dfs(num + 1, right(board_copy))
        elif i == 2:
            dfs(num + 1, up(board_copy))
        else:
            dfs(num + 1, down(board_copy))


dfs(0, board)
print(answer)
