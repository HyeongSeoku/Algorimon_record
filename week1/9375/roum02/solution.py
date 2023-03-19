import sys

test_case = int(sys.stdin.readline())


def solution():
    name, category = sys.stdin.readline().split()
    print(test_case, name, category)


# input case
for _ in range(test_case):
    clothes_number = int(sys.stdin.readline())
    for _ in range(clothes_number):
        solution()
