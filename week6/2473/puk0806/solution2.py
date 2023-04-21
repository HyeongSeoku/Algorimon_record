import sys

"""
풀이
- 숫자 리스트를 오름 차순으로 정렬
- 기준 하나를 잡고 2포인트를 통해서 특정 합을 찾는다.
    - 투포인터 O(N)
    - 현재 찾은 값보다 더 0에 근접한 값이면 갱신

"""


def input():
    return sys.stdin.readline().rstrip()


size = int(input())

ph_list = list(map(int, input().split(' ')))

ph_list.sort()

zero_sum = 3000000001
result = []

for i in range(0, size-2,1):
    j = i + 1
    z = size-1
    while (j < z):
        temp_sum = ph_list[i]+ph_list[j]+ph_list[z]
        if (zero_sum > abs(temp_sum)):
            zero_sum = abs(temp_sum)
            result = [ph_list[i], ph_list[j], ph_list[z]]
        if (temp_sum > 0):
            z -= 1
        elif (temp_sum < 0):
            j += 1
        else:
            print(result[0],result[1],result[2])
            exit(0)

print(result[0],result[1],result[2])
