i = sorted(list(__import__('sys').stdin.readline().rstrip()), reverse=True)
print(-1 if '0' not in i or sum(list(map(int, i))) % 3 != 0 else ''.join(i))
