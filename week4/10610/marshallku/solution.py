i = sorted(__import__('sys').stdin.readline().rstrip(), reverse=True)
print(-1 if '0' not in i or sum(map(int, i)) % 3 else ''.join(i))
