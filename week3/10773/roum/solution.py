"""
제로

1. 아이디어

0일 경우에는 앞에 있는 수 지우기

"""

import sys
read = sys.stdin.readline
k = int(read())
numbers = [int(read()) for _ in range(k)]
new_numbers = []

for number in numbers:
    if number == 0:
        new_numbers.pop()
    else:
        new_numbers.append(number)

print(sum(new_numbers))