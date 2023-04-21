import sys


def input():
    return sys.stdin.readline().rstrip()


size = int(input())

ph_list = list(map(int, input().split(' ')))

zero_sum = 3000000001
result = []

for i in range(0, size-2, 1):
    for j in range(i+1, size-1, 1):
        for z in range(j+1, size, 1):
            temp_sum = ph_list[i]+ph_list[j]+ph_list[z]

            if (abs(zero_sum) > abs(temp_sum)):
                zero_sum = temp_sum
                result = [ph_list[i], ph_list[j], ph_list[z]]


result.sort()
print(result)
