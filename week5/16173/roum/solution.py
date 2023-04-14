"""
점프왕 쩰리 ☄️

아이디어
1) 각 칸의 수를 stack에 넣는다
2) 오른쪽/아래쪽으로 가보고 더 이상 갈 수 없으면 넘어간다
"""

import sys

read = sys.stdin.readline

n = int(read())
matrix = [list(map(int, read().split(" "))) for _ in range(n)]


def go_jelly(y, x):
    # 쩰리가 위치한 수
    position_num = matrix[y][x]
    # 만약 출구에 도달했으면 종료
    if position_num == -1:
        return True

    # 오른쪽 또는 아래쪽의 좌표
    nx = x + position_num
    ny = y + position_num
    # matrix 범위 안에 있어야만 실행
    if nx < n and ny < n:
        # 오른쪽으로 진행하기
        value = go_jelly(y, nx)
        if value:
            go_jelly(y, nx)
        else:
            # 아래로 진행하기
            go_jelly(ny, x)
    # matrix 범위 안에 있지 않으면 실행 안함
    else:
        return False


for j in range(n):
    for i in range(n):
        go_jelly(j, i)
