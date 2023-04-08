"""
사냥꾼

아이디어
1. 동물의 좌표(a,b)에서 사대의 값의 범위에 사대의 값(x)이 있는지
a+b-l =< x =< a-b+l
2. 사대 좌표 리스트를 이진탐색한다.
"""
import sys

read = sys.stdin.readline

m, n, l = map(int, read().split(" "))
shoot_zone = list(map(int, read().split(" ")))
animals = [list(map(int, read().split(" "))) for _ in range(n)]
count = 0

# 이진탐색을 위해 정렬
shoot_zone.sort()

for a, b in animals:
    # b값이 l보다 크면 조기 종료
    if b > l:
        continue
    # 사대 값의 범위 구하기
    min_shoot = a + b - l
    max_shoot = a - b + l
    # 이진탐색
    start = 0
    end = m - 1
    while start <= end:
        mid = (start + end) // 2
        # 이진 탐색 수행 시, 사대 값의 범위 안에 존재한다면 동물 잡고 종료
        if shoot_zone[mid] >= min_shoot and shoot_zone[mid] <= max_shoot:
            count += 1
            break
            # 범위 안에 존재하지 않았다 => min_shoot이 더 크다 => mid값을 올려도 된다
        elif shoot_zone[mid] < max_shoot:
            start = mid + 1
        else:
            end = mid - 1

print(count)
