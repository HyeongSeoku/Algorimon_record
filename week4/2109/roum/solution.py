"""
순회강연

아이디어
-> day일 값이 같을 경우 pay 값이 가장 큰 값들의 합 -> hash

"""
import sys

read = sys.stdin.readline

n = int(read())
pay_day_list = [list(map(int, read().split(" "))) for _ in range(n)]


def make_dictionary():
    dictionary = {}
    for i in pay_day_list:
        pay, day = i
        # 같은 날이 있을 경우 최대값 저장
        if day in dictionary:
            max_value = max(dictionary[day], pay)
            dictionary[day] = max_value
        # 같은 날이 없을 경우 해당 값 저장 -> 리팩토링
        else:
            dictionary[day] = pay
    return dictionary


dictionary_value = make_dictionary()
total_value = sum(dictionary_value.values())
print(total_value)