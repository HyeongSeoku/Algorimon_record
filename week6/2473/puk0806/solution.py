import sys
import bisect

"""
정렬후 2개에를 묶고 나머지에 대해서 2진탐색 진행
여전히 느림 ...

Time Out O(N^2logN) 더 빨라야함 ..
두개 묶기 O(N^2)* 2진탐색O(logN)
"""


def input():
    return sys.stdin.readline().rstrip()


size = int(input())

ph_list = list(map(int, input().split(' ')))

zero_sum = 3000000001
result = []

for i in range(0, size-2, 1):
    for j in range(i+1, size-1, 1):
        temp_sum = ph_list[i]+ph_list[j]
        temp_ph_list = ph_list[j+1:]

        ph_index = bisect.bisect_left(temp_ph_list, -temp_sum)

        if (ph_index >= len(temp_ph_list)):
            ph_index = ph_index-1
        elif (ph_index < 0):
            ph_index = 0
        else:
            if (abs(temp_sum+temp_ph_list[ph_index-1]) < abs(temp_sum+temp_ph_list[ph_index])):
                ph_index -= 1

        temp_sum += temp_ph_list[ph_index]
        if (abs(zero_sum) > abs(temp_sum)):
            zero_sum = temp_sum
            result = [ph_list[i], ph_list[j], temp_ph_list[ph_index]]


result.sort()
print(result)
