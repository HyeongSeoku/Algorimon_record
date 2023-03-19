'''
    문제 이름 : 패션왕 신해빈
    문제 번호 : 9375
    문제 링크 : https://www.acmicpc.net/problem/9375
'''


def cloth_combination(cloth_dict):
    # 점화식 : (카테고리1의 개수 + 1) * (카테고리2의 개수 + 1) - 1
    result = 1
    for value in cloth_dict.values():
        result *= (value + 1)
    return result - 1


def dict_exist(dict, key):
    dict[key] = dict[key] + 1 if key in dict else 1


test_case_count = int(input())

for _ in range(test_case_count):
    cloth_count = int(input())
    cloth_dict = {}

    for _ in range(cloth_count):
        cloth_name, category = input().split()
        dict_exist(cloth_dict, category)

    print(cloth_combination(cloth_dict))
