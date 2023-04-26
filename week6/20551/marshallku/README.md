# Sort 마스터 배지훈의 후계자

```py
n, m = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])
```

Sort 마스터님의 뜻에 따라 오름차순으로 정렬한다.

```py
idx_map = {arr[i]: i for i in range(n) if i == 0 or arr[i] != arr[i-1]}
```

이미 정렬된 Array를 dictionary에 넣으므로, array에 그 값이 첫 번째로 등장할 때만(이전 값과 다른 값이면) 값을 덮어쓰면 된다.\
고로, 한 라인에 압축시킬 수 있다.

```py
for _ in range(m):
    print(idx_map.get(int(input()), -1))
```

`Dictionary.get()`을 활용하면 출력문도 삼항 연산 없이 깔끔하게 작성할 수 있다.
