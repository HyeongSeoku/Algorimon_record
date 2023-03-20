# Always override input
import sys

def input():
  return sys.stdin.readline().rstrip()

# Solution
for _ in range(int(input())):
    clothes = {}
    result = 1
    
    for _ in range(int(input())):
        name, cloth = input().split()
        clothes[cloth] = 1 if not cloth in clothes else clothes[cloth] + 1

    for cloth in clothes:
        # 각 의류를 안 입는 경우(1)를 더한 뒤
        result *= (clothes[cloth] + 1)

    # 모든 옷을 안 입는 경우(1) 제외
    print(result - 1)