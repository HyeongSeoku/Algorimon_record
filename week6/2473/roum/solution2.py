"""
세 용액
1) array 정렬시키기
2) fixedPoint, minPoint, maxPoint 합의 |최소값| 찾기
3) 반복문 진행
switch (true) {
    case sum < 0:
        minIndex = minIndex + 1
        break;
    case sum > 0:
        maxIndex = maxIndex - 1
        break;
    case sum === 0:
        answer = [fixedPoint, minPoint, maxPoint]
        break;
}

"""
import sys

read = sys.stdin.readline

n = int(read())
liquid_list = sorted(list(map(int, read().split())))

answer_list = []
min_value = 9999999999999999

for i in range(n-2):
    fixed_point = liquid_list[i]
    min_point = i + 1
    max_point = n - 1
    while min_point < max_point:
        sum_value = fixed_point + liquid_list[min_point] + liquid_list[max_point]
        if abs(sum_value) <= abs(min_value):
            min_value = abs(sum_value)
            answer_list = [fixed_point, liquid_list[min_point], liquid_list[max_point]]
        if sum_value < 0:
            min_point += 1
        elif sum_value > 0:
            max_point -= 1
        elif sum_value == 0:
            print(*answer_list)
            sys.exit()

print(*answer_list)




