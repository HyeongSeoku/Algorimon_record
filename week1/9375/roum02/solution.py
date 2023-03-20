import sys

test_case = int(sys.stdin.readline())


def make_dictionary():
    name, category = sys.stdin.readline().split()
    # category가 중복일 경우
    if category in dictionary:
        dictionary[category] += 1
    # category가 중복이 아닌 경우
    else:
        dictionary[category] = 1


def combination():
    result = 1
    for i in dictionary.values():
        result *= (i + 1)

    print(result - 1)


# input case
for _ in range(test_case):
    clothes_number = int(sys.stdin.readline())
    dictionary = {}
    for _ in range(clothes_number):
        make_dictionary()

    combination()
